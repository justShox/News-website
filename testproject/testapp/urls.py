from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registration', views.registration),
    path('add', views.add)
]
