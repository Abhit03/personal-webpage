from django.urls import include, path
from . import views

app_name = "listprojects"
urlpatterns = [
    path("", views.listprojects, name="listprojects"),
]
