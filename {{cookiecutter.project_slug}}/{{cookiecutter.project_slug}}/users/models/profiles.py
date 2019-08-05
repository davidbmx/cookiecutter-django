"""profile model"""

#django
from django.db import models

#utilities
from {{ cookiecutter.project_slug }}.utils.models import CRideModel


class Profile(CRideModel):
    """Profile model

    esta clase pasa a user apra la data publica
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )
    biography = models.TextField(max_length=500, blank=True)

    #stats
    rides_taken = models.PositiveIntegerField(default=0)
    rides_offered = models.PositiveIntegerField(default=0)
    reputation = models.FloatField(
        default=5.0,
        help_text='Users reputation based on the rides taken offered.'
    )

    def __str__(self):
        return str(self.user)
