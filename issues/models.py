from django.db import models
from core import models as core_models


class Attachment(core_models.CustomBaseModel):

    name = models.CharField(max_length=100)
    file = models.ImageField()
    issue = models.ForeignKey("issues.Issue", related_name="attachment", on_delete=models.CASCADE)


class Issue(core_models.CustomBaseModel):

    key = models.CharField(max_length=10, default=None, null=True)
    summary = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    reporter = models.ForeignKey("users.User", related_name="issues_reporter", on_delete=models.CASCADE)
    assignee = models.ForeignKey("users.User", related_name="issues_assignee", on_delete=models.SET_NULL, null=True, blank=True)
    project = models.ForeignKey("projects.Project", related_name="issue", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.summary}"

    def save(self, *args, **kwargs):
        # for generate pk
        super().save(*args, **kwargs)
        # create key value with self.pk
        self.key = f"{self.project.key}-{self.pk}"
        # save finally
        super().save(*args, **kwargs)
