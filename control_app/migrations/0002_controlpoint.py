# Generated by Django 5.2.1 on 2025-05-30 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process', models.CharField(max_length=255, verbose_name='Процесс')),
                ('control_action', models.CharField(max_length=255, verbose_name='Контрольное действие')),
                ('control_procedure', models.TextField(verbose_name='Контрольная процедура')),
                ('control_type', models.CharField(choices=[('preventive', 'Предотвращающий'), ('detective', 'Обнаруживающий')], max_length=20, verbose_name='Тип контроля')),
                ('frequency', models.CharField(max_length=100, verbose_name='Частота')),
                ('responsible_person', models.CharField(max_length=100, verbose_name='Ответственное лицо')),
                ('control_method', models.CharField(choices=[('manual', 'Ручной'), ('automated', 'Автоматический')], max_length=20, verbose_name='Метод контроля')),
                ('implemented', models.BooleanField(default=False, verbose_name='Контроль внедрён')),
            ],
        ),
    ]
