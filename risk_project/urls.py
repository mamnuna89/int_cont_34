from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from risk_app.views import RiskViewSet

router = DefaultRouter()
router.register(r'risks', RiskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
