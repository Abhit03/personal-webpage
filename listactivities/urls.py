from django.urls import path
from . import views

app_name = "listactivities"
urlpatterns = [
    path("", views.photogallery, name="photogallery"),
]
