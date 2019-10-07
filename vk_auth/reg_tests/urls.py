from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path("req_tests/", views.RegisterFormView.as_view()),
    path("req_tests/", views.LoginFormView.as_view()),
    path("req_tests/", views.LogoutFormView.as_view()),
    path("req_tests/", views.MainView.as_view()),
]
