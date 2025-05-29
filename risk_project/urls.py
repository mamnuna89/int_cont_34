from django.contrib import admin
from django.urls import path, include
from risk_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('risks/', include('risk_app.urls')),
    path('control/', include('control_app.urls')),
]