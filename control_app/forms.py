from django import forms
from .models import Risk

class RiskForm(forms.ModelForm):
    class Meta:
        model = Risk
        fields = [
            'name',
            'risk_type',
            'source',
            'registered_at',
            'department',
            'owner',
            'process',
            'probability',
            'impact',
        ]
