from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    username = models.CharField(max_length=51,verbose_name="Username kiriting",unique=True)
    last_name = False
    first_name = False
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    

    def get_absolute_url(self):
        return reverse('home')


