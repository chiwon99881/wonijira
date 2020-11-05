from django.db import models
from core import models as core_models


class Project(core_models.CustomBaseModel):

    name = models.CharField(max_length=150)
    key = models.CharField(max_length=10)
    leader = models.ForeignKey("users.User", related_name="project", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        to_upper_key = self.key.upper()
        self.key = to_upper_key
        super().save(*args, **kwargs)
