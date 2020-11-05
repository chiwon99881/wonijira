from django.db import models


class CustomBaseModel(models.Model):

    class Meta:
        abstract = True

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
