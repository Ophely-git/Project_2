from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    img = models.ImageField(upload_to='uploads/users_pictures/',default=None, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.username




