from django.contrib import admin
from . import models


@admin.register(models.UserGroup)
class UserGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    fields = ('username', 'email', 'avatar', 'first_name', 'last_name', 'groups')
    filter_horizontal = ('groups', )

    list_display = (
        'username',
        'email',
        'is_staff'
    )

    list_filter = (
        'is_staff',
        'username'
    )
