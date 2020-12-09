from django.db import models

# Create your models here.
class Apprenant(models.Model):
    nomApp=models.CharField(max_length=100)
    prenomApp=models.CharField(max_length=100)
    telApp=models.CharField(max_length=20)
    EmailApp=models.CharField(max_length=100)
    adresseApp=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.id}: {self.nomApp}, {self.prenomApp} ,{self.telApp}, {self.EmailApp}, {self.adresseApp}"

class Formateur(models.Model):
    nomF=models.CharField(max_length=100)
    prenomF=models.CharField(max_length=100)
    telF=models.CharField(max_length=20)
    EmailF=models.CharField(max_length=100)
    adresseF=models.CharField(max_length=100)
    profesionF=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: {self.nomF}, {self.prenomF} ,{self.telF}, {self.EmailF}, {self.adresseF}"

class Categorie(models.Model):
    categorie=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}: {self.categorie}"
    

class Formation(models.Model):
    nomcat=models.CharField(max_length=100)
    dateD=models.DateField('date')
    DateF=models.DateField('date')
    lieu=models.CharField(max_length=100)
    montant=models.IntegerField()
    idcategorie=models.ForeignKey(Categorie, on_delete=models.CASCADE)
    idFormateur=models.ForeignKey(Formateur, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.nomcat}, {self.dateD} ,{self.DateF}, {self.lieu}, {self.montant},{self.idcategorie},{self.idFormateur}"

class suivre(models.Model):
    heure=models.CharField(max_length=100)
    idApp=models.ForeignKey(Apprenant, on_delete=models.CASCADE)
    idFormation=models.ForeignKey(Formation, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id}: {self.heure}, {self.idApp} ,{self.idFormation}"