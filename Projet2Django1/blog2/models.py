from django.db import models
from phone_field import PhoneField
# Create your models here.
class Apprenant(models.Model):
    nomApp=models.CharField(max_length=100)
    prenomApp=models.CharField(max_length=100)
    telApp=PhoneField(blank=True, help_text='Contact phone number')
    EmailApp=models.EmailField(max_length=100,unique=True)
    adresseApp=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.id}: {self.nomApp}, {self.prenomApp} ,{self.telApp}, {self.EmailApp}, {self.adresseApp}"

class Formateur(models.Model):
    nomF=models.CharField(max_length=100)
    prenomF=models.CharField(max_length=100)
    telF=PhoneField(blank=True, help_text='Contact phone number')
    EmailF=models.EmailField(max_length=100,unique=True)
    adresseF=models.CharField(max_length=100)
    profesionF=models.CharField(max_length=100)

    def __str__(self):
        return f"identifiant: {self.id}: Nom de la formation:{self.nomF}, {self.prenomF} ,{self.telF}, {self.EmailF}, {self.adresseF}, {self.profesionF}"

class Categorie(models.Model):
    categorie=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return f"{self.id}: {self.categorie}"
    

class Formation(models.Model):
    nomcat=models.CharField(max_length=100)
    dateD=models.DateField('date')
    DateF=models.DateField('date')
    lieu=models.CharField(max_length=100)
    montant=models.IntegerField()
    Apprenant=models.ManyToManyField(Apprenant)
    idcategorie=models.ForeignKey(Categorie, on_delete=models.CASCADE)
    idFormateur=models.ForeignKey(Formateur, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.nomcat}, {self.dateD} ,{self.DateF}, {self.lieu}, {self.montant},{self.idcategorie},{self.idFormateur}"

