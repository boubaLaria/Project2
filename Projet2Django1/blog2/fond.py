from django import forms
from .models import Apprenant

class ApprenantForm(forms.ModelForm):


    class Meta:
        model = Apprenant
        fields = '__all__'
        labels = {
            'nomApp':'Nom',
            'prenomApp':'Prénom',
            'telApp':'Phone',
            'EmailApp':'Email',
            'QdresseApp':'Adresse',
        }
