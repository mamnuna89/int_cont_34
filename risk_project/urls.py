from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),         # Главная страница теперь из main_app
    path('risks/', include('risk_app.urls')),   # Модуль управления рисками
    path('control/', include('control_app.urls')),  # Модуль внутреннего контроля
]
