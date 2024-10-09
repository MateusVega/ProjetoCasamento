from django.urls import path
from . import views

app_name = "account"
urlpatterns = [
    path("", views.index, name="index"),
    path('register/', views.register_view, name='register'),
]