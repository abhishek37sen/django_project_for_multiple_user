from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_student = models.BooleanField('Is student', default=False)
    is_staff = models.BooleanField('Is staff', default=False)
    is_editor = models.BooleanField('Is editor', default=False)
    country = models.CharField(max_length=45)
    nationality = models.CharField(max_length=45)
    mobilenumber = models.IntegerField(default=None)
    # username = None
    email = models.EmailField('email address',unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
