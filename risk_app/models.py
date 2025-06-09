from control_app.models import Department
from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _

class Risk(models.Model):
    risk_code = models.CharField(_("Risk Code"), max_length=20, unique=True, blank=True)
    name = models.CharField(_("Name"), max_length=255)
    risk_type = models.CharField(_("Risk Type"), max_length=100)
    source = models.CharField(_("Source"), max_length=255)
    registered_at = models.DateField(_("Registration Date"))

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Department")
    )

    owner = models.CharField(_("Owner"), max_length=100)
    process = models.CharField(_("Process"), max_length=255)
    probability = models.IntegerField(_("Probability (1–5)"))
    impact = models.IntegerField(_("Impact (1–5)"))
    level = models.IntegerField(_("Risk Level"), blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.risk_code:
            count = Risk.objects.count() + 1
            year = datetime.now().year
            self.risk_code = f"RISK-2-{year}-{count:03d}"
        self.level = self.probability * self.impact
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
