from django.db import models

class Producto(models.Model):
    GENEROS = [
        ('Caballero', 'Caballero'),
        ('Dama', 'Dama'),
        ('Unisex', 'Unisex'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.CharField(max_length=50)
    genero = models.CharField(max_length=20, choices=GENEROS)
    fecha_creacion = models.DateField(auto_now_add=True)
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    marca = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.categoria})"