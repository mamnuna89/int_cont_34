from django.urls import path
from django.views.i18n import set_language
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('set-language/', set_language, name='set_language'),
]