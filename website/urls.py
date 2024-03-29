from django.urls import path
from . import views
from .models import *

farbe = Farben.objects.get(area="Hintergrund")
#bild = BilderFestlegen.objects.get(area="Startseite-Hauptbild")
context = {
    #"homeBild" : bild.image,
    "farbe" : farbe.farbcode,
    }
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('galerie', views.galerie, name='galerie'),
    path('<str:name>', views.singlePicView, name='picView' ),
]