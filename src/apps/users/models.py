import uuid
from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    did = models.CharField(max_length=250, unique=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    class Meta:
        db_table = 'users'
