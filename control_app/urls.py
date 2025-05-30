from django.urls import path
from . import views

urlpatterns = [
    path('', views.risk_list, name='control_risk_list'),
    path('add/', views.risk_create, name='control_risk_create'),
    path('add/', views.risk_create, name='risk_create')
    path('', views.control_index, name='control_index'),
    path('risks/', views.risk_list, name='control_risk_list'),
    path('risks/add/', views.risk_create, name='control_risk_create'),
    path('control-points/add/', views.control_point_create, name='control_point_create'),
]