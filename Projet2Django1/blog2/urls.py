from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name="home"),
    path("<int:id>",views.home,name="apprenantmodif"),
    path("<int:id>",views.apprenantdelete,name="apprenantdelete"),
    path("apprenantliste",views.apprenantliste,name="apprenantliste"),
    
]