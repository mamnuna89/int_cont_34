from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Department, Division

class DivisionInline(admin.TabularInline):
    model = Division
    extra = 1

@admin.register(Department)
class DepartmentAdmin(TranslationAdmin):  # ⬅️ используем TranslationAdmin
    inlines = [DivisionInline]
    list_display = ['name']

@admin.register(Division)
class DivisionAdmin(TranslationAdmin):  # ⬅️ обязательно для Division тоже
    list_display = ['name', 'department']
