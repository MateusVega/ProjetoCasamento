from django.urls import path
from . import views

app_name = "menusel"
urlpatterns = [
    path("", views.form, name="form"),
    path("menu", views.menu, name="menu"),
    path("invite", views.invite, name="invite"),
    path("review", views.review, name="review"),
]