from django.urls import path
from .views import index, success

urlpatterns = [
    path('', index, name="home"),
    path('success/', success, name="success"),
]