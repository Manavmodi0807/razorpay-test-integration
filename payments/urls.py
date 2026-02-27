from django.urls import path
from .views import index, success, webhook

urlpatterns = [
    path('', index, name="home"),
    path('success/', success, name="success"),
    path('webhook/', webhook, name="webhook"),
]