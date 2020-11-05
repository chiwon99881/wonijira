from django.contrib import admin
from . import models


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'key',
        'leader'
    )

    list_filter = (
        'name',
        'key',
    )
