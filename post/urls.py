from django.urls import path
from .views import (
    list_view,detail_view,
    PostCreateView,PostUpdateView,
    PostDeletView,HomeView)

from .views import (
    list_ustoz_view,list_shogird_view,
    list_sherig_view,list_hodim_view,
    list_ishchi_view,
)



urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('list/',list_view,name='list'),
    path('post/<int:pk>/delete/',PostDeletView.as_view(),name='post_delete'),
    path('post/<slug:slug>/edit/',PostUpdateView.as_view(),name='post_edit'),
    path('post/new/',PostCreateView.as_view(),name='post_new'),
    path('post/<slug:slug>/',detail_view,name='post_detail'),
    
    ## shuyerdan pasti def orqali yasalgan view lar uchun
    path('list/ustoz/',list_ustoz_view,name='list_ustoz'),
    path('list/shogird/',list_shogird_view, name='list_shogird'),
    path('list/sherig/',list_sherig_view, name='list_sherig'),
    path('list/hodim/',list_hodim_view, name='list_hodim'),
    path('list/ishchi/',list_ishchi_view, name='list_ishchi'),
    
]
