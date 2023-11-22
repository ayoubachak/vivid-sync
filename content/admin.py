from django.contrib import admin

# Register your models here.
from .models import Content

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'profile', 'posted_date')
    list_filter = ('profile', 'posted_date')
    search_fields = ('title', 'description')