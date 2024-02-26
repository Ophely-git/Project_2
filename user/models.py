from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ExtendUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ext')
    img = models.ImageField(upload_to='uploads/users_pictures/',blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)