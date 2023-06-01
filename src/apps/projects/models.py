import uuid
from django.db import models


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=5, null=True)
    loan_amount = models.IntegerField()
