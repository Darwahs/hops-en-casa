from email.policy import default
from django.db import models
from .persona import Persona
from .profesional_salud import Profesional_salud
from .familiar_paciente import FamiliarPaciente
from .choices import options_rh

class Departamento(models.Model):
    id_dep = models.BigAutoField(primary_key = True, null = False, db_column = 'Id_dep')
    nom_dep = models.CharField('Departamento', max_length=100, unique = True, db_column = 'Nom_dep', null = False)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
    
    def __str__(self):
        return self.nom_dep

class Ciudad(models.Model):
    id_ciudad = models.BigAutoField(primary_key = True, null = False, db_column = 'Id_ciudad')
    id_dep = models.ForeignKey(Departamento, related_name = 'Departamento', on_delete = models.CASCADE,
    db_column='Id_dep')
    nom_ciudad = models.CharField('Ciudad', max_length=100, db_column = 'Nom_ciudad')

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
    
    def __str__(self):
        return self.nom_ciudad

class Paciente(models.Model):
    id_pac = models.OneToOneField(Persona, on_delete = models.CASCADE, null = False, primary_key = True,
    db_column = 'Id_pac', related_name = 'Paciente')
    fech_nac = models.DateField('Fecha De Nacimiento', null = False, db_column = 'Fech_nac')
    rh_pac = models.CharField('Grupo Sanguíneo', max_length = 3, choices = options_rh, db_column = 'Rh_pac')
    id_fam = models.OneToOneField(FamiliarPaciente, on_delete = models.CASCADE, null = False, db_column = "Id_fam",
    verbose_name = 'Familiar del paciente')
    id_pro = models.ForeignKey(Profesional_salud, on_delete = models.CASCADE, db_column = 'Id_pro',
    verbose_name = 'Profesional de la salud')
    dir_pac = models.CharField('Direccion', max_length = 200, db_column = 'Dir_pac')
    id_ciudad = models.ForeignKey(Ciudad, on_delete = models.CASCADE, db_column = 'Id_ciudad',
    verbose_name = 'Ciudad')
    lon_pac = models.CharField('Longitud', max_length = 60, default = "Sin Registro", null = False, db_column = 'Lon_pac')
    lat_pac = models.CharField('Latitud', max_length = 60, default = "Sin Registro", null = False, db_column = 'Lat_pac')

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
    
    def __str__(self):
        return str(self.id_pac)+' '+str(self.id_pro)+' '+str(self.id_ciudad)