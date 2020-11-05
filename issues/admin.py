from django.contrib import admin
from . import models


class AttachmentInline(admin.TabularInline):

    model = models.Attachment


@admin.register(models.Issue)
class IssueAdmin(admin.ModelAdmin):

    inlines = [AttachmentInline, ]

    fields = (
        'project',
        'summary',
        'description',
        'reporter',
        'assignee',
    )

    list_display = (
        'key',
        'summary',
        'project',
        'reporter'
    )

    list_display_links = (
        'key',
        'summary'
    )
