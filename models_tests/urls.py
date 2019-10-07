from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path("models_tests/", views.models_tests, name='models_tests'),
]
