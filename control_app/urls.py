from django.urls import path
from . import views
from .views import (
    department_structure,
    process_map_overview,
    control_export_risks_excel,
)
from .views import export_control_points_excel
from .views import control_point_edit
from .views import control_point_delete
urlpatterns = [
    path('', views.control_index, name='control_index'),
    path('structure/', department_structure, name='department_structure'),

    # 👉 Реестр рисков
    path('risks/', views.risk_list, name='control_risk_list'),
    path('risks/add/', views.risk_create, name='control_risk_create'),
    path('risks/<int:pk>/edit/', views.risk_edit, name='control_risk_edit'),
    path('risks/<int:pk>/delete/', views.risk_delete, name='control_risk_delete'),

    # 👉 Контрольные точки
    path('control-points/', views.control_point_list, name='control_point_list'),
    path('control-points/add/', views.control_point_create, name='control_point_create'),

    # 👉 Карта процессов и редактор
    path('process-map/', process_map_overview, name='process_map_overview'),
    path('diagrams/', views.diagram_list, name='diagram_list'),
    path('diagrams/save/', views.save_process_diagram, name='save_process_diagram'),
    path('bpmn/editor/', views.editor_view, name='editor_bpmn'),

    # 👉 Экспорт
    path('control/export/', control_export_risks_excel, name='control_export_risks_excel'),
    path('control-points/export/', export_control_points_excel, name='export_control_points_excel'),
     path('control-points/edit/<int:pk>/', control_point_edit, name='control_point_edit'),
     path('control-points/delete/<int:pk>/', control_point_delete, name='control_point_delete'),
]
