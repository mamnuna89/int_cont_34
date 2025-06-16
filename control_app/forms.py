from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Risk, ControlPoint, Department

class RiskForm(forms.ModelForm):
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        empty_label=_("Select Department"),
        widget=forms.Select(attrs={'class': 'form-select'})
    )

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
            'related_risk',
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
            'related_risk': _('Related Risk'),
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['related_risk'].queryset = Risk.objects.none()

        if 'process' in self.data:
            process_value = self.data.get('process')
            if process_value:
                self.fields['related_risk'].queryset = Risk.objects.filter(process__iexact=process_value)
        elif self.instance.pk and self.instance.process:
            self.fields['related_risk'].queryset = Risk.objects.filter(process__iexact=self.instance.process)

    def clean(self):
        cleaned_data = super().clean()
        process = cleaned_data.get('process')
        control_action = cleaned_data.get('control_action')
        control_procedure = cleaned_data.get('control_procedure')
        division = cleaned_data.get('division')

        if ControlPoint.objects.filter(
            process=process,
            control_action=control_action,
            control_procedure=control_procedure,
            division=division
        ).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                _("A control point with the same process, action, procedure and division already exists.")
            )
