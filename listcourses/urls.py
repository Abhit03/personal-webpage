from django.urls import include, path
from . import views

app_name = "listcourses"
urlpatterns = [
    path("", views.listcourses, name="listcourses"),
]
