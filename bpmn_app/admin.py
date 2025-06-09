from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import ProcessDiagram

@admin.register(ProcessDiagram)
class ProcessDiagramAdmin(admin.ModelAdmin):  # можно также использовать TranslationAdmin, если нужны переводы
    list_display = ['name', 'department', 'division', 'created_at', 'created_by']
    list_filter = ['department', 'division']
    search_fields = ['name']
