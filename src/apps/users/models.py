import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    did = models.CharField(max_length=250, unique=True)
    access_token = models.CharField(max_length=512, unique=True)
    refresh_access_token = models.CharField(max_length=512, unique=True)
    country = models.CharField(max_length=5, null=True)

    class Meta:
        db_table = 'users'

    def save(self, *args, **kwargs):
        if not self.username:
            username = get_random_string(length=10)

            # Ensure the username is unique
            while User.objects.filter(username=username).exists():
                username = get_random_string(length=10)

            self.username = username

        super().save(*args, **kwargs)
