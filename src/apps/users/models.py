import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string
from django_countries.fields import CountryField


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    did = models.CharField(max_length=250, unique=True)
    access_token = models.CharField(max_length=512, unique=True)
    refresh_access_token = models.CharField(max_length=512, unique=True)
    country = CountryField(null=True)

    class Meta:
        db_table = 'users'

    @property
    def name(self):
        if not self.first_name and not self.last_name:
            return self.username
        return '%s %s' % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        if not self.username:
            username = get_random_string(length=10)

            # Ensure the username is unique
            while User.objects.filter(username=username).exists():
                username = get_random_string(length=10)

            self.username = username

        super().save(*args, **kwargs)
