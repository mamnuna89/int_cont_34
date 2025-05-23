from django.contrib import admin
from django.urls import path
from risk_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('risks/', views.risk_list, name='risk_list'),
    path('risks/add/', views.risk_create, name='risk_create'),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
