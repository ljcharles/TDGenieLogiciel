from django.db import models

# Create your models here.
class Classe(models.Model):
    """docstring for Classe."""
    nom = models.CharField(max_length=200)

class Ordre(models.Model):
    """docstring for Ordre."""
    nom = models.CharField(max_length=200)
    classe = models.ForeignKey(Classe,models.CASCADE)

class Famille(models.Model):
    """docstring for Famille."""
    nom = models.CharField(max_length=200)
    ordre = models.ForeignKey(Ordre,models.CASCADE)

class Animal(models.Model):
    """docstring for Animal."""
    nomVernaculaire = models.CharField(max_length=200)
    nomScientifique = models.CharField(max_length=200)
    famille = models.ForeignKey(Famille,models.CASCADE)
