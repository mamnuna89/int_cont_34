from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_list, name='process_map_overview'),
    path('diagrams/', views.diagram_list, name='diagram_list'),
]
