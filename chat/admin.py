from django.contrib import admin
from .models import Message
# Register your models here.

@admin.register(Message)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'room', 'content', 'date_added')