from django.shortcuts import render
from .models import CustomUser
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from .forms import CustomUserCreationForm

# Create your views here.




class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserProfileView(UpdateView):
    model = CustomUser
    template_name = 'post_profile.html'
    fields = ['username','email']

    

