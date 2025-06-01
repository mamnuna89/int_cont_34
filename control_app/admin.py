from django.contrib import admin
from .models import Department, Division

class DivisionInline(admin.TabularInline):
    model = Division
    extra = 1

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    inlines = [DivisionInline]
    list_display = ['name']