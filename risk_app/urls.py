from django.urls import path, include
from . import views

app_name = 'risk_app'

urlpatterns = [
    path('', views.risk_list, name='risk_list'),
    path('add/', views.risk_create, name='risk_create'),
    path('risk/matrix/', views.risk_matrix_view, name='risk_matrix'),
]