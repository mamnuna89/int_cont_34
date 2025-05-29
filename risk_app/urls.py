from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.risk_create, name='risk_create'),
    path('', views.risk_list, name='risk_list'),
]
