"""Users app."""

#Django
from django.apps import AppConfig

class UsersConfig(AppConfig):
    """Users app config"""

    name = '{{ cookiecutter.project_slug }}.users'
    verbose_name = 'Users'