from django.contrib import admin
from . import models


class AttachmentInline(admin.TabularInline):

    model = models.Attachment


@admin.register(models.Issue)
class IssueAdmin(admin.ModelAdmin):

    # Foreign Key를 이용하여 search_fieldds 또는 list_filter를 사용하려하면
    # 해당 필드의 어떤 값을 원하는지 명확하게 명시해줘야 한다.
    # 예를 들면 하기와 같이 'project__name' 이런식으로 프로젝트 이름으로 필터링을 원하는 것
    list_filter = (
        'project__name',
        'reporter__username',
    )

    search_fields = (
        "project__name",
        "summary",
        "key__iexact",
        "reporter__username__iexact"
    )

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
