from django.urls import path
from . import views
from .views import (
    department_structure,
    process_map_overview,
    control_export_risks_excel,
    export_control_points_excel,
    control_point_edit,
    control_point_delete,
)

urlpatterns = [
    # 👉 Главная
    path('', views.control_index, name='control_index'),

    # 👉 Структура департаментов
    path('structure/', department_structure, name='department_structure'),

    # 👉 Реестр рисков
    path('risks/', views.risk_list, name='control_risk_list'),
    path('risks/add/', views.risk_create, name='control_risk_create'),
    path('risks/<int:pk>/edit/', views.risk_edit, name='control_risk_edit'),
    path('risks/<int:pk>/delete/', views.risk_delete, name='control_risk_delete'),

    # 👉 Контрольные точки
    path('control-points/', views.control_point_list, name='control_point_list'),
    path('control-points/add/', views.control_point_create, name='control_point_create'),
    path('control-points/edit/<int:pk>/', control_point_edit, name='control_point_edit'),
    path('control-points/delete/<int:pk>/', control_point_delete, name='control_point_delete'),

    # 👉 Карта процессов и схемы
    path('process-map/', process_map_overview, name='process_map_overview'),
    path('diagrams/', views.diagram_list, name='diagram_list'),
    path('diagrams/view/<int:diagram_id>/', views.diagram_view, name='diagram_view'),
    path('diagrams/edit/<int:diagram_id>/', views.edit_diagram, name='edit_diagram'),
    path('diagrams/delete/<int:diagram_id>/', views.delete_diagram, name='delete_diagram'),
    path('diagrams/save/', views.save_process_diagram, name='save_process_diagram'),
    path('bpmn/editor/', views.editor_view, name='editor_bpmn'),

    # 👉 Экспорт
    path('control/export/', control_export_risks_excel, name='control_export_risks_excel'),
    path('control-points/export/', export_control_points_excel, name='export_control_points_excel'),

    # 👉 AJAX
    path('ajax/get-risks-by-process/', views.get_risks_by_process, name='get_risks_by_process'),
]
