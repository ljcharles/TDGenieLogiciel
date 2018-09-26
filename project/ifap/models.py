from django.db import models

# Create your models here.
class Classe(models.Model):
    """docstring for Classe."""
    nom = models.CharField(max_length=200)

    def getNom(self):
        return self.nom

class Ordre(models.Model):
    """docstring for Ordre."""
    nom = models.CharField(max_length=200)
    classe = models.ForeignKey(Classe,models.CASCADE)

    def getNom(self):
        return self.nom

    def getClasse(self):
        return self.classe

class Famille(models.Model):
    """docstring for Famille."""
    nom = models.CharField(max_length=200)
    ordre = models.ForeignKey(Ordre,models.CASCADE)

    def getNom(self):
        return self.nom

    def getOrdre(self):
        return self.ordre

class Animal(models.Model):
    """docstring for Animal."""
    nomVernaculaire = models.CharField(max_length=200)
    nomScientifique = models.CharField(max_length=200)
    famille = models.ForeignKey(Famille,models.CASCADE)

    def getNomVernaculaire(self):
        return self.nomVernaculaire

    def getNomScientifique(self):
        return self.nomScientifique

    def getFamille(self):
        return self.famille
