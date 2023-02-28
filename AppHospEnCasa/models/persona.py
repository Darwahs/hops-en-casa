from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from .choices import sexos, roles

class TipoDocumento(models.Model):
    id_doc = models.AutoField(primary_key = True, null = False, db_column = 'Id_doc')
    tipo_doc = models.CharField('Tipo de documento',max_length=150, null = False, unique = True,
    db_column = 'Tipo_doc')

    class Meta:
        verbose_name = 'Tipo_documento'
        verbose_name_plural = 'Tipos_documentos'
    
    def __str__(self):
        return self.tipo_doc

class UserManager(BaseUserManager):

    def create_user(self, username, password = None):
        if not username:
            raise ValueError('El usuario debe contener \"username\"')
        usuario = self.model(username=username)
        usuario.set_password(password)
        usuario.save(using=self._db)

        return usuario

    def create_superuser(self, username, password):
        usuario = self.create_user(username=username, password=password)
        usuario.is_admin = True
        usuario.save(using = self._db)

        return usuario

class RolPersona(models.Model):
    id_rol = models.BigAutoField(primary_key=True, null = False, db_column = 'Id_rol')
    nom_rol = models.CharField('Rol', max_length = 100, choices = roles, null = False, db_column = 'Nom_rol')

    class Meta:
        verbose_name = 'Rol_persona'
        verbose_name_plural = 'Rol_personas'
    
    def __str__(self):
        return self.nom_rol+' '+str(self.id_per)

class Persona(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key = True, null = False, db_column = 'Id_per')
    nom_per = models.CharField('Nombres', max_length = 100, null = False, db_column = 'Nombre')
    primerApe_per = models.CharField('Primer Apellido', max_length = 100, null = False, db_column = 'Pri_apellido')
    segundoApe_per = models.CharField('Segundo Apellido', max_length = 100, null = False, db_column = 'Seg_apellido')
    telefono = models.CharField('Teléfono', max_length = 25, null = False, db_column = 'Teléfono')
    id_doc = models.ForeignKey(TipoDocumento, on_delete = models.CASCADE, null = False, db_column = 'Id_doc',
    verbose_name = 'Id documento')
    numdoc_per = models.CharField('Número de documento', max_length = 25, null = False, db_column = 'Numero_doc',
    unique = True)
    gen_per = models.CharField('Género', max_length = 1, null = False, choices = sexos, db_column = 'Género')
    password = models.CharField('Contraseña', max_length = 256, null = False, db_column = 'Contraseña')
    last_login = models.DateTimeField(null = True, db_column = 'Último Ingreso')
    is_superuser = models.BooleanField(default = False, db_column = 'Superuser')

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.numdoc_per, some_salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'numdoc_per'

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return self.nom_per+' '+self.primerApe_per+' '+self.segundoApe_per