from django.urls import path
from .views import orchestrator

urlpatterns = [
    path('', orchestrator)
]