from django.urls import path
from . import views

urlpatterns = [
    path('', views.control_index, name='control_index'),
    path('risks/', views.risk_list, name='control_risk_list'),
    path('risks/add/', views.risk_create, name='control_risk_create'),
    path('control-points/', views.control_point_list, name='control_point_list'),
    path('control-points/add/', views.control_point_create, name='control_point_create'),
]
