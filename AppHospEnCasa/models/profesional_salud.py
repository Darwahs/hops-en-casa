from django.db import models
from .persona import Persona

class Especialidad(models.Model):
    id_esp = models.BigAutoField(primary_key=True, null = False, db_column = 'Id_esp')
    nom_esp = models.CharField('Especialidad', max_length = 150, null = False, unique = True,
    db_column = 'Especialidad')

    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'
    
    def __str__(self):
        return self.nom_esp

class Profesional_salud(models.Model):
    id_pro = models.OneToOneField(Persona, on_delete = models.CASCADE, null = False, primary_key = True,
    db_column = 'Id_pro', related_name = 'Profesional_salud')
    id_esp = models.ForeignKey(Especialidad, on_delete = models.CASCADE, db_column = 'Id_esp',
    verbose_name = 'Especialidad')
    tarj_pro = models.CharField('Tarjeta Profesional', max_length = 50, db_column = 'Tarj_pro', null = False)

    class Meta:
        verbose_name = 'Profesional_salud'
        verbose_name_plural = 'Profesionales_salud'
    
    def __str__(self):
        return str(self.id_pro)+' '+str(self.id_esp)