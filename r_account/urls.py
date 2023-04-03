from .views import SignUpView,UserProfileView
from django.urls import path, include


urlpatterns = [
    path('signup/',SignUpView.as_view(),name='signup'),
    path('profile/<int:pk>/',UserProfileView.as_view(),name='profile')
]

