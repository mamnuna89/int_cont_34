from django.urls import path
from . import views

urlpatterns = [
    path('', views.risk_list, name='control_risk_list'),
    path('add/', views.risk_create, name='control_risk_create'),
]