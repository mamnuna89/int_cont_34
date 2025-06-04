from django.db import models

class Department(models.Model):
    name = models.CharField("Департамент", max_length=200, unique=True)

    def __str__(self):
        return self.name

class Division(models.Model):
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='control_points', null=True, blank=True)
    name = models.CharField("Отдел", max_length=200)

    def __str__(self):
        return f"{self.department.name} – {self.name}"
