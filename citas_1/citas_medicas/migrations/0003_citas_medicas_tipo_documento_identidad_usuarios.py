# Generated by Django 4.2.1 on 2023-06-03 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas_medicas', '0002_doctores_especialidades_paciente'),
    ]

    operations = [
        migrations.CreateModel(
            name='citas_medicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cita_id', models.CharField(max_length=10)),
                ('paciente_id', models.CharField(max_length=10)),
                ('fecha_cita', models.CharField(max_length=30)),
                ('especialidad_id', models.CharField(max_length=10)),
                ('doctor_id', models.CharField(max_length=10)),
                ('observaciones', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_documento_identidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_documento_id', models.CharField(max_length=10)),
                ('tipo_documento_nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('fullname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=60)),
            ],
        ),
    ]
