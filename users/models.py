from django.db import models
from django.contrib.auth.models import AbstractUser
from core import models as core_models


class UserGroup(core_models.CustomBaseModel):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class User(AbstractUser):

    avatar = models.ImageField(blank=True, null=True)
    groups = models.ManyToManyField(UserGroup, related_name="user")
