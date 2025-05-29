from django.urls import path
from . import views

urlpatterns = [
    path('risks/', views.risk_list, name='risk_list'),
    path('risks/add/', views.risk_create, name='risk_create'),
]
