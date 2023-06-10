import uuid
import math
from datetime import datetime
from django.utils import timezone
from django.conf import settings
from django.db import models
from django_countries.fields import CountryField
from src.utils.crypto_trx_verify import verify_transaction
from src.apps.users.models import User


class Project(models.Model):
    RATE = 1.3
    LIVE_DAYS = 30
    STATUS_PENDING = 'PENDING'
    STATUS_COMPLETE = 'COMPLETE'
    STATUS_FUNDRAISING = 'FUNDRAISING'
    STATUS_EXPIRED = 'EXPIRED'

    STATUS_CHOICES = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_COMPLETE, 'Compelete'),
        (STATUS_FUNDRAISING, 'Fundraising'),
        (STATUS_EXPIRED, 'expired')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    subtitle = models.TextField()
    description = models.TextField()
    location = CountryField(null=True)
    loan_amount = models.IntegerField()
    repayment_period = models.IntegerField()
    reach_goal_amount = models.IntegerField(null=True)
    status = models.CharField(
        max_length=16, choices=STATUS_CHOICES, default=STATUS_PENDING)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    @property
    def monthly_payback_amount(self):
        return math.ceil(self.loan_amount / self.repayment_period * 100 * self.RATE) / 100

    @property
    def total_payback_amount(self):
        return math.ceil(self.loan_amount * 100 * self.RATE) / 100

    @property
    def reach_goal_percent(self):
        return 100 - ((self.reach_goal_amount * 100) / self.loan_amount)

    @property
    def live_remains(self):
        return self.LIVE_DAYS - (timezone.now() - self.created_at).days

    def save(self, *args, **kwargs):
        if self.reach_goal_amount is None or self.reach_goal_amount > self.loan_amount:
            self.reach_goal_amount = self.loan_amount
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'projects'


class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField()
    project = models.ForeignKey(
        Project, related_name='images', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'photos'


class Withdrawn(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    total_amount = models.IntegerField()
    transaction_id = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    @classmethod
    def borrowing(cls, project, user, source, destination, amount, transaction_id):
        verfied = verify_transaction(
            source, destination, amount, transaction_id)
        if not verfied:
            raise Exception('transaction is not valid')
        withdrawn = cls(
            user=user,
            project=project,
            total_amount=amount,
            transaction_id=transaction_id,
        )
        withdrawn.save()

        Lend.objects.filter(project=project).update(
            status=Lend.STATUS_LENDED,
            withdrawn=withdrawn
        )

        project.status = Project.STATUS_COMPLETE
        project.save()

    def save(self, *args, **kwargs):
        Lend.objects.filter(project=self.project).update(
            status=Lend.STATUS_LENDED)
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'withrawns'


class Lend(models.Model):
    STATUS_PENDING = 'PENDING'
    STATUS_LENDED = 'LENDED'
    STATUS_REFUNDED = 'REFUNDED'

    STATUS_CHOICES = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_LENDED, 'Lended'),
        (STATUS_REFUNDED, 'Refunded')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, related_name='lends',
                             on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(
        Project, related_name='lends', on_delete=models.SET_NULL, null=True)
    withdrawn = models.ForeignKey(
        Withdrawn, related_name='lends', on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    transaction_id = models.CharField(max_length=300)
    refund_transaction_id = models.CharField(max_length=300, null=True)

    status = models.CharField(
        max_length=16, choices=STATUS_CHOICES, default=STATUS_PENDING)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    @classmethod
    def lending(cls, project, user, source, amount, transaction_id):
        verfied = verify_transaction(
            source, settings.BLOCKCHAIN_CONTRACT, amount, transaction_id)
        if not verfied:
            raise Exception('transaction is not valid')
        cls(
            user=user,
            project=project,
            amount=amount,
            transaction_id=transaction_id,
        ).save()

    def save(self, *args, **kwargs):
        if self.refund_transaction_id:
            self.status = self.STATUS_REFUNDED
        self.updated_at = datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'lends'
