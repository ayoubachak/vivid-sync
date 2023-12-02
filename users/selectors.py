from django.db.models.query import QuerySet

from .filters import BaseUserFilter
from .models import VividUser


def user_get_login_data(*, user: VividUser):
    return {
        "id": user.id,
        "email": user.email,
        "is_active": user.is_active,
        "is_admin": user.is_admin,
        "is_superuser": user.is_superuser,
    }


def user_list(*, filters=None) -> QuerySet[VividUser]:
    filters = filters or {}

    qs = VividUser.objects.all()

    return BaseUserFilter(filters, qs).qs