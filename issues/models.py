from django.db import models
from core import models as core_models


class Attachment(core_models.CustomBaseModel):

    name = models.CharField(max_length=100)
    file = models.ImageField()
    issue = models.ForeignKey("issues.Issue", related_name="attachment", on_delete=models.CASCADE)


class Issue(core_models.CustomBaseModel):

    summary = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    reporter = models.ForeignKey("users.User", related_name="issues_reporter", on_delete=models.CASCADE)
    assignee = models.ForeignKey("users.User", related_name="issues_assignee", on_delete=models.SET_NULL, null=True, blank=True)
