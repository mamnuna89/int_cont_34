from django.db import models

RISK_TYPES = [
    ('стратегический', 'Стратегический'),
    ('корпоративный', 'Корпоративный'),
    ('операционный', 'Операционный'),
]

class Risk(models.Model):
    description = models.TextField('Описание')
    risk_type = models.CharField('Тип риска', max_length=50, choices=RISK_TYPES)
    risk_owner = models.CharField('Владелец риска', max_length=100)
    process = models.CharField('Процесс', max_length=100)
    department = models.CharField('Подразделение', max_length=100)
    likelihood = models.IntegerField('Вероятность (1-5)')
    impact = models.IntegerField('Воздействие (1-5)')

    @property
    def risk_level(self):
        return self.likelihood * self.impact

    def __str__(self):
        return self.description
