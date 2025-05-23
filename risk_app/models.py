from django.db import models

RISK_TYPES = [
    ('стратегический', 'Стратегический'),
    ('корпоративный', 'Корпоративный'),
    ('операционный', 'Операционный'),
]

from django.db import models

class Risk(models.Model):
    name = models.CharField("Название", max_length=255)
    risk_type = models.CharField("Тип риска", max_length=100)
    source = models.CharField("Источник", max_length=255)
    description = models.TextField("Описание")
    registered_at = models.DateField("Дата регистрации")
    department = models.CharField("Подразделение", max_length=100)
    owner = models.CharField("Владелец риска", max_length=100)
    process = models.CharField("Процесс", max_length=255)
    probability = models.IntegerField("Вероятность (1–5)")
    impact = models.IntegerField("Воздействие (1–5)")
    level = models.IntegerField("Уровень риска", blank=True, null=True)
    assessment_history = models.TextField("История оценки", blank=True)
    attachment = models.FileField("Прикреплённые документы", upload_to='attachments/', blank=True, null=True)
    measures = models.TextField("Меры по устранению риска", blank=True)

    def save(self, *args, **kwargs):
        self.level = self.probability * self.impact
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
