from django.urls import path, include
from rest_framework import routers
from .views import PostApiView , UserApiView


router = routers.DefaultRouter()
router.register(r'ser_api', UserApiView, basename='ser_api')
router.register(r'drift_api', PostApiView, basename='drift_api')

urlpatterns = [
    path('',include(router.urls)),
]


