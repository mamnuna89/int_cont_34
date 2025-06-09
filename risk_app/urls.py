from django.urls import path, include
from . import views

app_name = 'risk_app'

urlpatterns = [
    path('', views.risk_list, name='risk_list'),
    path('add/', views.risk_create, name='risk_create'),
    path('risk/<int:risk_id>/', views.risk_detail, name='risk_detail'),  # ✏️ Редактирование
    path('risk/<int:pk>/edit/', views.risk_update, name='risk_update'),
    path('risk/<int:risk_id>/delete/', views.risk_delete, name='risk_delete'),  # 🗑 Удаление
    path('risk/matrix/', views.risk_matrix_view, name='risk_matrix'),
]