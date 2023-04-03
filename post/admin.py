from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Post)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['name','address','drift','slug','status','author','created_at']
    list_filter = ['drift','address','author']
    list_editable = ['status',]




@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','username','status','created_at']
    list_filter = ['post','username']
    list_editable = ['status',]
    search_fields = ['post','username']






