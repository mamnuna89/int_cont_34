# Generated by Django 5.2.1 on 2025-06-04 11:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_app', '0006_alter_controlpoint_department'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessDiagram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название схемы')),
                ('bpmn_xml', models.TextField(verbose_name='XML-содержимое схемы')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Создано пользователем')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_app.department', verbose_name='Департамент')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_app.division', verbose_name='Отдел')),
            ],
        ),
    ]
