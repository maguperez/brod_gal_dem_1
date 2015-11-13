from django.db import models


# Create your models here.

class Empresa(models.Model):
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
        return self.descripcion


class Puesto(models.Model):
    descripcion = models.CharField(max_length="50")

    def __unicode__(self):
        return self.descripcion
