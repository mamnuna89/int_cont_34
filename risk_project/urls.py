from django.contrib import admin
from django.urls import path, include
from risk_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('risks/', include('risk_app.urls')),
    path('control/', include('control_app.urls')),
]