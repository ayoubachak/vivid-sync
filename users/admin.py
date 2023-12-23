from django.contrib import admin

from users.models import VividUser

# Register your models here.
class VividUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'account_type','is_staff', 'email_verified', 'agreed_to_terms')  # Add 'email_verified'
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login', 'email_verified')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# Register your models here.
admin.site.register(VividUser, VividUserAdmin)