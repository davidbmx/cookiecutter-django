from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from {{ cookiecutter.project_slug }}.users.models import User, Profile

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_client')
    list_filter = ('is_client', 'is_staff', 'created', 'modified')


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)