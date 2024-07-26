from django.db      import models
from empresa.models import Empresa

class Empleado(models.Model):
    id              = models.BigAutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    fecharegistro   = models.DateTimeField(db_column='fecha_registro', blank=False, null=False)  # Field name made lowercase.
    empresaid       = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='empresa_id')  # Field name made lowercase.
    rut             = models.IntegerField(db_column='rut', blank=False, null=False)  # Field name made lowercase.
    dv              = models.CharField(db_column='dv', max_length=1, blank=False, null=False)  # Field name made lowercase.
    nombres         = models.CharField(db_column='nombres', max_length=255, blank=False, null=False)  # Field name made lowercase.
    apellidouno     = models.CharField(db_column='apellido_uno', max_length=255, blank=False, null=False)  # Field name made lowercase.
    apellidodos     = models.CharField(db_column='apellido_dos', max_length=255, blank=False, null=False)  # Field name made lowercase.
    email           = models.CharField(db_column='email', max_length=255, blank=False, null=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empleado'
