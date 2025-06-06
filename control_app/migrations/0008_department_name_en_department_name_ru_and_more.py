# Generated by Django 5.2.1 on 2025-06-06 17:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_app', '0007_processdiagram'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='name_en',
            field=models.CharField(max_length=200, null=True, unique=True, verbose_name='Department'),
        ),
        migrations.AddField(
            model_name='department',
            name='name_ru',
            field=models.CharField(max_length=200, null=True, unique=True, verbose_name='Department'),
        ),
        migrations.AddField(
            model_name='division',
            name='name_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Division'),
        ),
        migrations.AddField(
            model_name='division',
            name='name_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Division'),
        ),
        migrations.AlterField(
            model_name='controlpoint',
            name='control_action',
            field=models.CharField(max_length=255, verbose_name='Control Action'),
        ),
        migrations.AlterField(
            model_name='controlpoint',
            name='control_method',
            field=models.CharField(choices=[('manual', 'Manual'), ('automated', 'Automated')], max_length=20, verbose_name='Control Method'),
        ),
        migrations.AlterField(
            model_name='controlpoint',
            name='control_procedure',
            field=models.TextField(verbose_name='Control Procedure'),
        ),
        migrations.AlterField(
            model_name='controlpoint',
            name='control_type',
            field=models.CharField(choices=[('preventive', 'Preventive'), ('detective', 'Detective')], max_length=20, verbose_name='Control Type'),
        ),
        migrations.AlterField(
            model_name='controlpoint',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='control_app.division', verbose_name='Division'),
        ),
        migrations.AlterField(
            model_name='controlpoint',
            name='frequency',
            field=models.CharField(max_length=100, verbose_name='Frequency'),
        ),
        migrations.AlterField(
            model_name='controlpoint',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='controlpoint',
            name='implemented',
            field=models.BooleanField(default=False, verbose_name='Implemented'),
        ),
        migrations.AlterField(
            model_name='controlpoint',
            name='process',
            field=models.CharField(max_length=255, verbose_name='Process'),
        ),
        migrations.AlterField(
            model_name='controlpoint',
            name='responsible_person',
            field=models.CharField(max_length=100, verbose_name='Responsible Person'),
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='division',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='division',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Division'),
        ),
        migrations.AlterField(
            model_name='processdiagram',
            name='bpmn_xml',
            field=models.TextField(verbose_name='BPMN XML Content'),
        ),
        migrations.AlterField(
            model_name='processdiagram',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='processdiagram',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AlterField(
            model_name='processdiagram',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_app.department', verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='processdiagram',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_app.division', verbose_name='Division'),
        ),
        migrations.AlterField(
            model_name='processdiagram',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='processdiagram',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Diagram Name'),
        ),
        migrations.AlterField(
            model_name='risk',
            name='department',
            field=models.CharField(max_length=100, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='risk',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='risk',
            name='impact',
            field=models.IntegerField(verbose_name='Impact (1–5)'),
        ),
        migrations.AlterField(
            model_name='risk',
            name='level',
            field=models.IntegerField(blank=True, null=True, verbose_name='Risk Level'),
        ),
        migrations.AlterField(
            model_name='risk',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='risk',
            name='owner',
            field=models.CharField(max_length=100, verbose_name='Risk Owner'),
        ),
        migrations.AlterField(
            model_name='risk',
            name='probability',
            field=models.IntegerField(verbose_name='Probability (1–5)'),
        ),
        migrations.AlterField(
            model_name='risk',
            name='process',
            field=models.CharField(max_length=255, verbose_name='Process'),
        ),
        migrations.AlterField(
            model_name='risk',
            name='registered_at',
            field=models.DateField(verbose_name='Registration Date'),
        ),
        migrations.AlterField(
            model_name='risk',
            name='risk_code',
            field=models.CharField(blank=True, max_length=20, unique=True, verbose_name='Risk Code'),
        ),
        migrations.AlterField(
            model_name='risk',
            name='risk_type',
            field=models.CharField(max_length=100, verbose_name='Risk Type'),
        ),
        migrations.AlterField(
            model_name='risk',
            name='source',
            field=models.CharField(max_length=255, verbose_name='Source'),
        ),
    ]
