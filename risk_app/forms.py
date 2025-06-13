from django import forms
from .models import Risk
from django.utils.translation import gettext_lazy as _

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

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        department = cleaned_data.get('department')
        process = cleaned_data.get('process')

        if name and department and process:
            # Проверка на дубликат
            qs = Risk.objects.filter(name=name, department=department, process=process)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)

            if qs.exists():
                # Добавляем ошибку в поля
                self.add_error('name', _("Duplicate risk with this name, department, and process."))
                self.add_error('department', "")
                self.add_error('process', "")
