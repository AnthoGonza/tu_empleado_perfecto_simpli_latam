from django.db import models

class Empresa(models.Model):
    id              = models.BigAutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    fecharegistro   = models.DateTimeField(db_column='fecha_registro', blank=False, null=False)  # Field name made lowercase.
    rut             = models.IntegerField(db_column='rut', blank=False, null=False)  # Field name made lowercase.
    dv              = models.CharField(db_column='dv', max_length=1, blank=False, null=False)  # Field name made lowercase.
    nombre          = models.CharField(db_column='nombre', max_length=255, blank=False, null=False)  # Field name made lowercase.
    direccion       = models.CharField(db_column='direccion', max_length=255, blank=False, null=False)  # Field name made lowercase.
    telefono        = models.IntegerField(db_column='telefono', blank=False, null=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa'
