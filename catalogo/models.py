from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    tecnologia = models.CharField(max_length=100)
    fecha = models.DateField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['-fecha']
