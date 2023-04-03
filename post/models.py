from django.db import models
from django.urls import reverse
from django.utils import timezone
from r_account.models import CustomUser
from autoslug import AutoSlugField
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your models here.

tanlov = (
    ('ustoz','Ustoz kerak'),
    ('shogird','Shogird kerak'),
    ('hodim','Hodim kerak'),
    ('ish_joyi','Ish joyi kerak'),
    ('sherig','Sherig kerak'),
)

class Post(models.Model):
    drift = models.CharField(max_length=100,choices=tanlov)
    name = models.CharField(max_length=130,verbose_name="Ism familyangiz")
    slug = AutoSlugField(populate_from='name',unique=True)
    age = models.PositiveIntegerField(verbose_name="Yoshingiz")
    address = models.CharField(max_length=300,verbose_name="Manzilingiz")
    technology = models.CharField(max_length=500,verbose_name="Texnologiya, men",help_text='..larni bilaman')
    jobs = models.CharField(max_length=300,verbose_name="Kasp")
    price = models.CharField(max_length=100,verbose_name="Talab qilinadigan summa")
    application_time = models.CharField(max_length=51,verbose_name="Murojat qilish vaqti")
    phone = models.CharField(max_length=120,verbose_name="Bog'lanish uchun tel nomer")
    photo = models.ImageField(upload_to='photo/%Y/%m/',default='default/ustoz_shogird.jpg', blank=True, null=True)
    title = models.TextField(verbose_name="Qo'shimcha malumot")
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='account')

    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
     
    def get_absolute_url(self):
        return reverse('list')





class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    username = models.CharField(max_length=41)
    body = models.CharField(max_length=310,verbose_name='Comment qoldiring')
    created_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
   
    def __str__(self) -> str:
        return self.username
