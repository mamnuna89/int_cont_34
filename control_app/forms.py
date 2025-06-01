from django import forms
from .models import Risk, ControlPoint

class RiskForm(forms.ModelForm):
    class Meta:
        model = Risk
        fields = [
            'name', 'risk_type', 'source', 'registered_at',
            'department', 'owner', 'process', 'probability', 'impact'
        ]

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
        labels = {
            'process': 'Процесс',
            'control_action': 'Контрольное действие',
            'control_procedure': 'Контрольная процедура',
            'control_type': 'Тип контроля',
            'frequency': 'Частота',
            'responsible_person': 'Ответственное лицо',
            'control_method': 'Метод контроля',
            'implemented': 'Контроль внедрён',
        }
        widgets = {
            'control_type': forms.Select(choices=[
                ('preventive', 'Предотвращающий'),
                ('detective', 'Обнаруживающий'),
            ]),
            'control_method': forms.Select(choices=[
                ('manual', 'Ручной'),
                ('automated', 'Автоматический'),
            ]),
        }
