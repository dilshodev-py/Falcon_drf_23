from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, EmailField


# Create your models here.


class User(AbstractUser):
    phone = CharField(max_length=12)
    email = EmailField()
