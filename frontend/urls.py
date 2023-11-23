from django.urls import path
from . import views

urlpatterns = [
    # React Frontend
    path('test', views.index, name='index'),

    # Django templates
    path('', views.landing_page, name='landing_page'),
]
