from django.db import models

# Create your models here.

class paciente(models.Model):
    paciente_id = models.CharField(max_length=10)
    tipo_documento_id = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    fecha_nacimiento = models.CharField(max_length=50)
    tipo_seguro_id = models.CharField(max_length=10)

class doctores(models.Model):
    doctor_id = models.CharField(max_length=10)
    doctor_nombre = models.CharField(max_length=50)
    doctor_telefono = models.CharField(max_length=30)
    fecha_nacimiento = models.CharField(max_length=50)
    
   
    
class especialidades(models.Model):
    especialidad_id = models.CharField(max_length=10)
    especialidad_nombre = models.CharField(max_length=50)

class usuarios(models.Model):
    username = models.CharField(max_length=10)
    fullname = models.CharField(max_length=30)
    email = models.CharField(max_length=20)
    telefono = models.CharField(max_length=60)


        

    
class tipos_seguro(models.Model):
    tipo_seguro_id = models.CharField(max_length=10)
    tipo_seguro_nombre = models.CharField(max_length=50)

class tipo_documento_identidad(models.Model):
    tipo_documento_id = models.CharField(max_length=10)
    tipo_documento_nombre = models.CharField(max_length=50)


class citas_medicas(models.Model):
    cita_id = models.CharField(max_length=10)
    paciente_id = models.CharField(max_length=10)
    fecha_cita = models.CharField(max_length=30)
    especialidad_id = models.CharField(max_length=10)
    doctor_id =  models.CharField(max_length=10)
    observaciones = models.CharField(max_length=30)
    username = models.CharField(max_length=30)

    