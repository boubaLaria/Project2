from django.contrib import admin

# Register your models here.
from .models import Apprenant,Formation,Formateur,Categorie

admin.site.register(Apprenant)
admin.site.register(Formation)
admin.site.register(Formateur)
admin.site.register(Categorie)

