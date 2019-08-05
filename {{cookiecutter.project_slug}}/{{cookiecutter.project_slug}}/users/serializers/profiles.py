from rest_framework import serializers

from {{ cookiecutter.project_slug }}.users.models import Profile

class ProfileModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'