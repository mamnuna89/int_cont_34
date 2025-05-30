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
            'action',
            'procedure',
            'control_type',
            'frequency',
            'responsible',
            'method',
            'is_implemented',
        ]

        labels = {
            'process': 'Процесс',
            'action': 'Контрольное действие',
            'procedure': 'Контрольная процедура',
            'control_type': 'Тип контроля',
            'frequency': 'Частота',
            'responsible': 'Ответственное лицо',
            'method': 'Метод контроля',
            'is_implemented': 'Контроль внедрён',
        }

        widgets = {
            'control_type': forms.Select(choices=[
                ('preventive', 'Предотвращающий'),
                ('detective', 'Обнаруживающий'),
            ]),
            'method': forms.Select(choices=[
                ('manual', 'Ручной'),
                ('automated', 'Автоматический'),
            ]),
        }
