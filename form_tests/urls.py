from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path("form_tests/", views.form_tests, name='form_tests'),
    path("search/", views.search, name='search'),
    path("form_tests/", views.file_input, name='file_input'),
]
