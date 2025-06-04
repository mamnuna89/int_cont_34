from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField("Департамент", max_length=200, unique=True)

    def __str__(self):
        return self.name

class Division(models.Model):
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='divisions')
    name = models.CharField("Отдел", max_length=200)

    def __str__(self):
        return f"{self.department.name} – {self.name}"

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
            self.risk_code = f"CTRL-{year}-{count:03d}"
        self.level = self.probability * self.impact
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class ControlPoint(models.Model):
    CONTROL_TYPE_CHOICES = [
        ('preventive', 'Предотвращающий'),
        ('detective', 'Обнаруживающий'),
    ]

    CONTROL_METHOD_CHOICES = [
        ('manual', 'Ручной'),
        ('automated', 'Автоматический'),
    ]

    process = models.CharField("Процесс", max_length=255)
    control_action = models.CharField("Контрольное действие", max_length=255)
    control_procedure = models.TextField("Контрольная процедура")
    control_type = models.CharField("Тип контроля", max_length=20, choices=CONTROL_TYPE_CHOICES)
    frequency = models.CharField("Частота", max_length=100)
    responsible_person = models.CharField("Ответственное лицо", max_length=100)
    control_method = models.CharField("Метод контроля", max_length=20, choices=CONTROL_METHOD_CHOICES)
    implemented = models.BooleanField("Контроль внедрён", default=False)

    division = models.ForeignKey('Division', verbose_name="Отдел", on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='control_points')


    def save(self, *args, **kwargs):
        if self.division:
            self.department = self.division.department
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.process} — {self.control_action}"

class ProcessDiagram(models.Model):
    name = models.CharField("Название схемы", max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Департамент")
    division = models.ForeignKey(Division, on_delete=models.CASCADE, verbose_name="Отдел")
    bpmn_xml = models.TextField("XML-содержимое схемы")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Создано пользователем")

    def __str__(self):
        return self.name
