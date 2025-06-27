from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from control_app import views as control_views

# 👇 Добавлено: отдельный маршрут для смены языка
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

# 👇 Основные маршруты с поддержкой мультиязычности
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    
    path('', include('main_app.urls')),              # Главная страница
    path('risks/', include('risk_app.urls')),        # Управление рисками
    path('control/', include('control_app.urls')),   # Внутренний контроль
    # Только редактор используется из control_app
path('bpmn/editor/', control_views.editor_view, name='editor_bpmn'),
)
