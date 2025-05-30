from django import forms
from .models import Risk

class RiskForm(forms.ModelForm):
    class Meta:
        model = Risk
        fields = [
            'name', 'risk_type', 'source', 'registered_at',
            'department', 'owner', 'process', 'probability', 'impact'
        ]
        from django import forms
from .models import ControlPoint

class ControlPointForm(forms.ModelForm):
    class Meta:
        model = ControlPoint
        fields = [
            'process',
            'control_action',
            'control_procedure',
            'control_type',
            'frequency',
            'responsible_person',
            'control_method',
            'implemented',
        ]
        widgets = {
            'control_type': forms.Select(),
            'control_method': forms.Select(),
        }
