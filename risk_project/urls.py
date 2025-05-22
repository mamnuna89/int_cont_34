from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from rest_framework.routers import DefaultRouter
from risk_app.views import RiskViewSet

router = DefaultRouter()
router.register(r'risks', RiskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', lambda request: render(request, 'index.html')),
]
path('risks/', lambda request: render(request, 'risk_list.html')),
