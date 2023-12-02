import django_filters
from .models import VividUser

class BaseUserFilter(django_filters.FilterSet):
    class Meta:
        model = VividUser
        fields = ("id", "email")