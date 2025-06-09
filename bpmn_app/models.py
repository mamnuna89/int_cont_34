from django.db import models
from django.contrib.auth.models import User
from control_app.models import Department, Division  # связь с контрольным модулем

class ProcessDiagram(models.Model):
    name = models.CharField("Название схемы", max_length=255)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        verbose_name="Департамент",
        related_name="bpmn_diagrams"  # 🔧 уникальное имя для связи
    )

    division = models.ForeignKey(
        Division,
        on_delete=models.CASCADE,
        verbose_name="Отдел",
        related_name="bpmn_diagrams"  # 🔧 уникальное имя для связи
    )

    bpmn_xml = models.TextField("XML-содержимое схемы")

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Создано пользователем",
        related_name="bpmn_created_diagrams"  # 🔧 уникальное имя
    )

    def __str__(self):
        return self.name
