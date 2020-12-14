from django.shortcuts import render,redirect
from .models import Apprenant,Formateur
from .fond import ApprenantForm


def home(request,id=0):
    if request.method=="GET":
        if id==0:
            form =ApprenantForm()
        else:
            apprenant=Apprenant.objects.get(pk=id)
            form =ApprenantForm(instance=apprenant)
        return render(request,"index.html",{
         "form":form,
          })

    else:
        if id==0:
            form =ApprenantForm(request.POST)
        else:
             apprenant=Apprenant.objects.get(pk=id)
             form=ApprenantForm(request.POST,instance=apprenant)
        if form.is_valid():
            form.save()
        return redirect('apprenantliste')

   
def apprenantliste(request):
    contenant= {'apprenantliste':Apprenant.objects.all()}
    return render(request,"teste.html",contenant )

def apprenantdelete(request,id):
    apprenant=Apprenant.objects.get(pk=id)
    apprenant.delete()
    return redirect('apprenantliste')