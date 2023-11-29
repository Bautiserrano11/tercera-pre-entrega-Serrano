from django.db import models

class Libro(models.Model):
    # Atributos del modelo

    objects = models.Manager()

class Pelicula(models.Model):
    # Atributos del modelo

    objects = models.Manager()

class Autor(models.Model):
    # Atributos del modelo

    objects = models.Manager()