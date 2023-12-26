from django.contrib import admin
from .models import Organization, Industry  # Adjust the import path according to your project structure

# Register your models here.
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin', 'website', 'phone', 'year_founded')
    search_fields = ('name', 'city', 'country', 'admin__username')
    list_filter = ('country', 'city', 'industries')
    ordering = ('name',)
    raw_id_fields = ('admin',)
    fieldsets = (
        (None, {
            'fields': ('name', 'admin', 'description', 'tagline')
        }),
        ('Contact Information', {
            'fields': ('address', 'city', 'country', 'phone', 'website')
        }),
        ('Details', {
            'fields': ('image', 'banner', 'organization_size', 'organization_type', 'year_founded', 'industries')
        }),
    )

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Industry)
