from django.contrib import admin
from .models import Risk

admin.site.register(Risk)
class RiskAdmin(admin.ModelAdmin):
    list_display = ['risk_code', 'name', 'risk_type', 'owner', 'department', 'level']
    search_fields = ['name', 'risk_code', 'owner']
    list_filter = ['risk_type', 'department']