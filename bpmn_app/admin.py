from django.contrib import admin
from .models import ProcessDiagram

@admin.register(ProcessDiagram)
class ProcessDiagramAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'division', 'created_at', 'created_by']
    list_filter = ['department', 'division']
    search_fields = ['name']
