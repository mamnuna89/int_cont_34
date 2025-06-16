from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Department(models.Model):
    name = models.CharField(_("Department"), max_length=200, unique=True)

    def __str__(self):
        return self.name

class Division(models.Model):
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='divisions')
    name = models.CharField(_("Division"), max_length=200)

    def __str__(self):
        return f"{self.department.name} – {self.name}"

class Risk(models.Model):
    risk_code = models.CharField(_("Risk Code"), max_length=20, unique=True, blank=True)
    name = models.CharField(_("Name"), max_length=255)
    risk_type = models.CharField(_("Risk Type"), max_length=100)
    source = models.CharField(_("Source"), max_length=255)
    registered_at = models.DateField(_("Registration Date"))
    department = models.CharField(_("Department"), max_length=100)
    owner = models.CharField(_("Risk Owner"), max_length=100)
    process = models.CharField(_("Process"), max_length=255)
    probability = models.IntegerField(_("Probability (1–5)"))
    impact = models.IntegerField(_("Impact (1–5)"))
    level = models.IntegerField(_("Risk Level"), blank=True, null=True)

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
        ('preventive', _("Preventive")),
        ('detective', _("Detective")),
    ]

    CONTROL_METHOD_CHOICES = [
        ('manual', _("Manual")),
        ('automated', _("Automated")),
    ]

    process = models.CharField(_("Process"), max_length=255)
    related_risk = models.ForeignKey(
        Risk,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="linked_control_points",
        verbose_name=_("Related Risk")
    )
    control_action = models.CharField(_("Control Action"), max_length=255)
    control_procedure = models.TextField(_("Control Procedure"))
    control_type = models.CharField(_("Control Type"), max_length=20, choices=CONTROL_TYPE_CHOICES)
    frequency = models.CharField(_("Frequency"), max_length=100)
    responsible_person = models.CharField(_("Responsible Person"), max_length=100)
    control_method = models.CharField(_("Control Method"), max_length=20, choices=CONTROL_METHOD_CHOICES)
    implemented = models.BooleanField(_("Implemented"), default=False)

    division = models.ForeignKey('Division', verbose_name=_("Division"), on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='control_points')

    def save(self, *args, **kwargs):
        if self.division:
            self.department = self.division.department
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.process} — {self.control_action}"

    @property
    def related_risk_code(self):
        return self.related_risk.risk_code if self.related_risk else ""

    @property
    def related_risk_name(self):
        return self.related_risk.name if self.related_risk else ""

class ProcessDiagram(models.Model):
    name = models.CharField(_("Diagram Name"), max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name=_("Department"))
    division = models.ForeignKey(Division, on_delete=models.CASCADE, verbose_name=_("Division"))
    bpmn_xml = models.TextField(_("BPMN XML Content"))
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name=_("Created By"))

    def __str__(self):
        return self.name
