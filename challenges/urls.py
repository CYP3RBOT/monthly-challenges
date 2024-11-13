from django.urls import path

from . import views

urlpatterns = [
    path("january/", views.january),
    path("febuary/", views.febuary),
]
