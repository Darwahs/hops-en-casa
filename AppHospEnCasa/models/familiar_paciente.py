from django.db import models
from .persona import Persona

class FamiliarPaciente(models.Model):
    id_fam = models.OneToOneField(Persona, null = False, on_delete = models.CASCADE, primary_key = True,
    db_column = 'Id_per')
    paren_fam = models.CharField('Parentesco', max_length = 20, null = True, db_column = 'Paren_fam')
    email_fam = models.EmailField('Correo Del Familiar', db_column = 'Email_fam', null = False)

    class Meta:
        verbose_name = 'Familiar_paciente'
        verbose_name_plural = 'Familiar_pacientes'
    
    def __str__(self):
        return str(self.id_fam)+' '+str(self.id_par)+' '+str(self.id_pac)