from django.db import models
from .paciente import Paciente

class HistoriaClinica(models.Model):
    id_hiscli = models.BigAutoField(primary_key = True, db_column = 'Id_hiscli')
    id_pac = models.OneToOneField(Paciente, on_delete = models.CASCADE, db_column = 'Id_pac',
    verbose_name = 'Paciente')
    diag_hiscli = models.TextField('Diagnostico', null = True, db_column = 'Id_diag')
    
    class Meta:
        verbose_name = 'Historia_clinica'
        verbose_name_plural = 'Historias_clinicas'
    
    def __str__(self):
        return str(self.id_pac)+' '+str(self.id_diag)

class Sugerencia(models.Model):
    id_sug = models.BigAutoField(primary_key = True, null = False, db_column = 'Id_sug')
    id_hiscli = models.ForeignKey(HistoriaClinica, on_delete = models.CASCADE, db_column = 'id_hiscli',
    verbose_name = 'Historia Clínica')
    nom_sug = models.CharField('Sugerencia', max_length = 200)
    descript_sug = models.TextField('Descripción De Sugerencia', db_column = 'Descript_sug')
    fecha_sug = models.DateTimeField("Fecha De Sugerencia", db_column = 'Fecha_sug')

    class Meta:
        verbose_name = 'Sugerencias'
        verbose_name_plural = 'Sugerencias'
    
    def __str__(self):
        return str(self.id_hiscli)+' '+self.nom_sug