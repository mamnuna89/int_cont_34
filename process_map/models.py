from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Division(models.Model):
    department = models.ForeignKey(Department, related_name='divisions', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.department.name} – {self.name}"
