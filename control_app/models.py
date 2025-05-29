from django.db import models
from datetime import datetime

class Risk(models.Model):
    risk_code = models.CharField("Код риска", max_length=20, unique=True, blank=True)
    name = models.CharField("Название", max_length=255)
    risk_type = models.CharField("Тип риска", max_length=100)
    source = models.CharField("Источник", max_length=255)
    registered_at = models.DateField("Дата регистрации")
    department = models.CharField("Подразделение", max_length=100)
    owner = models.CharField("Владелец риска", max_length=100)
    process = models.CharField("Процесс", max_length=255)
    probability = models.IntegerField("Вероятность (1–5)")
    impact = models.IntegerField("Воздействие (1–5)")
    level = models.IntegerField("Уровень риска", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.risk_code:
            count = Risk.objects.count() + 1
            year = datetime.now().year
            self.risk_code = f"RISK-2-{year}-{count:03d}"
        self.level = self.probability * self.impact
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
