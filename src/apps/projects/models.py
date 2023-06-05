import uuid
from django.db import models
from src.apps.users.models import User


class Project(models.Model):
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
    location = models.CharField(max_length=5, null=True)
    loan_amount = models.IntegerField()
    repayment_period = models.IntegerField()
    status = models.CharField(
        max_length=16, choices=STATUS_CHOICES, default=STATUS_PENDING)

    class Meta:
        db_table = 'projects'


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
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    transaction_id = models.CharField(max_length=300)
    refund_transaction_id = models.CharField(max_length=300)

    status = models.CharField(
        max_length=16, choices=STATUS_CHOICES, default=STATUS_PENDING)

    @staticmethod
    def reach_goal_amount(project):
        loans = Lend.objects.filter(project_id=project.id).all()
        amount = project.loan_amount
        print(amount, '******************')
        for loan in loans:
            amount -= loan.amount

        return amount

    def save(self, *args, **kwargs):
        if self.refund_transaction_id:
            self.status = self.STATUS_REFUNDED
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'lends'


class Withdrawn(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    total_amount = models.IntegerField()
    transaction_id = models.CharField(max_length=300)

    def save(self, *args, **kwargs):
        Lend.objects.filter(project=self.project).update(
            status=Lend.STATUS_LENDED)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'withrawns'
