from django.db import models
from .historia_clinica import HistoriaClinica

class Tipo_Signo_Vital(models.Model):
    id_tipsig = models.BigAutoField(primary_key = True, db_column = 'Id_tipsig')
    nom_tipsig = models.CharField('Tipo De Signo Vital', max_length = 150, db_column = 'Nom_tipsig')

    class Meta:
        verbose_name = 'Tipo_signo_vital'
        verbose_name_plural = 'Tipos_signos_vitales'
    
    def __str__(self):
        return self.nom_tipsig

class Signo_Vital(models.Model):
    id_sigvi = models.BigAutoField(primary_key = True, db_column = 'Id_sigvi')
    id_tipsig = models.ForeignKey(Tipo_Signo_Vital, on_delete = models.CASCADE, db_column = 'Id_tipsig',
    verbose_name = 'Signo Vital')
    id_hiscli = models.ForeignKey(HistoriaClinica, on_delete = models.CASCADE, db_column = 'Id_hiscli',
    verbose_name = 'Historia Clínica')
    medicion_sig = models.DecimalField('Medición Del Signo Vital', max_digits = 3, decimal_places = 3,
    db_column = 'Medicion_sig')
    fecha_sig = models.DateTimeField('Fecha De Seguimiento', null = False, db_column = 'Fecha_sig')

    class Meta:
        verbose_name = 'Signo_vital'
        verbose_name_plural = 'Signos_vitales'
    
    def __str__(self):
        return str(self.id_tipsig)+' '+str(self.id_hiscli)