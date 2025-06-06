from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Risk, ControlPoint

class RiskForm(forms.ModelForm):
    class Meta:
        model = Risk
        fields = [
            'name', 'risk_type', 'source', 'registered_at',
            'department', 'owner', 'process', 'probability', 'impact'
        ]
        labels = {
            'name': _('Name'),
            'risk_type': _('Risk Type'),
            'source': _('Source'),
            'registered_at': _('Registration Date'),
            'department': _('Department'),
            'owner': _('Risk Owner'),
            'process': _('Process'),
            'probability': _('Probability'),
            'impact': _('Impact'),
        }

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
            'division',
        ]
        labels = {
            'process': _('Process'),
            'control_action': _('Control Action'),
            'control_procedure': _('Control Procedure'),
            'control_type': _('Control Type'),
            'frequency': _('Frequency'),
            'responsible_person': _('Responsible Person'),
            'control_method': _('Control Method'),
            'implemented': _('Implemented'),
            'division': _('Division'),
        }
        widgets = {
            'control_type': forms.Select(choices=[
                ('preventive', _('Preventive')),
                ('detective', _('Detective')),
            ]),
            'control_method': forms.Select(choices=[
                ('manual', _('Manual')),
                ('automated', _('Automated')),
            ]),
        }
