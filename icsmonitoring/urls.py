from django.urls import path

from . import views

app_name='icsmonitoring'
urlpatterns = [
    path("", views.icsmonitoringhome, name="icsmonitoringhome"),
]