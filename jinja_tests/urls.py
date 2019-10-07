from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path("main_page/", views.main_page, name='main_page'),
    path("contact/", views.contact, name='contact'),
    path("about/", views.about, name='about'),
    path("news/", views.news, name='news'),
]
