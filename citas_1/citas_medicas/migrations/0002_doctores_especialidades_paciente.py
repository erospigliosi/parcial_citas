# Generated by Django 4.2.1 on 2023-06-03 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas_medicas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.CharField(max_length=10)),
                ('doctor_nombre', models.CharField(max_length=50)),
                ('doctor_telefono', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='especialidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad_id', models.CharField(max_length=10)),
                ('especialidad_nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente_id', models.CharField(max_length=10)),
                ('tipo_documento_id', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=60)),
                ('state_province', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.CharField(max_length=50)),
                ('tipo_seguro_id', models.CharField(max_length=10)),
            ],
        ),
    ]
