from django.urls import path
from .views import bpmn_editor

urlpatterns = [
    path('editor/', bpmn_editor, name='bpmn_editor'),
]
