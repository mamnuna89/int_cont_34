from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.risk_list, name='risk_list'),
    path('add/', views.risk_create, name='risk_create'),
]