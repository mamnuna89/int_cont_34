from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.control_index, name='control_index'),  # Главная страница модуля
    path('risks/', views.risk_list, name='control_risk_list'),  # Список рисков
    path('risks/add/', views.risk_create, name='control_risk_create'),  # Добавить риск
    path('control-points/add/', views.control_point_create, name='control_point_create'),  # Добавить контрольную точку
]
