import uuid
from django.db import models
from src.apps.users.models import User


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    subtitle = models.TextField()
    description = models.TextField()
    location = models.CharField(max_length=5, null=True)
    loan_amount = models.IntegerField()
    repayment_period = models.IntegerField()

    class Meta:
        db_table = 'projects'
