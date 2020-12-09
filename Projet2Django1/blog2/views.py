from django.shortcuts import render
from .models import Apprenant

def home(request,):
    return render(request,"index.html",{
        "affichageA":Apprenant.objects.all()
    
    })

