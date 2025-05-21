from django.db import models

class Risk(models.Model):
    number = models.AutoField(primary_key=True)
    description = models.TextField()
    risk_type = models.CharField(max_length=50)
    risk_owner = models.CharField(max_length=100)
    process = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    likelihood = models.IntegerField()
    impact = models.IntegerField()
    level = models.IntegerField(editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.level = self.likelihood * self.impact
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Risk #{self.number}"
