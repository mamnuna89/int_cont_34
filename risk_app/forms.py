from django import forms
from .models import Risk

class RiskForm(forms.ModelForm):
    class Meta:
        model = Risk
        fields = ['description', 'risk_type', 'risk_owner', 'process', 'department', 'likelihood', 'impact']
