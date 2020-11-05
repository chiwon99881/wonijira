from django.contrib import admin
from . import models


class AttachmentInline(admin.TabularInline):

    model = models.Attachment


@admin.register(models.Issue)
class IssueAdmin(admin.ModelAdmin):

    inlines = (AttachmentInline,)
