from django.contrib import admin
from django.urls import path, include
from control_app import views as control_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('process-map/', include('process_map.urls')),
    path('', include('main_app.urls')),         # Главная страница теперь из main_app
    path('risks/', include('risk_app.urls')),   # Модуль управления рисками
    path('control/', include('control_app.urls')),  # Модуль внутреннего контроля
    path('bpmn/editor/', control_views.editor_view, name='editor_bpmn'),
]
