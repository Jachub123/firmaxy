from django.shortcuts import render
from .models import *
from PIL import Image
from PIL.ExifTags import TAGS
from django.views.generic.base import TemplateView
from django.core.management import call_command

# Create your views here.

def variables():
    hintergrund = Farben.objects.get(area="Hintergrund")
    fontAcryl = Farben.objects.get(area="Head1_Schrift_Acryl")
    headVorname = Farben.objects.get(area="Head2_Schrift_Evita")
    headNachname2 = Farben.objects.get(area="Head4_Schrift_Nonne2")
    navLinks = Farben.objects.get(area="Navbar_Verlinkungen")
    stripe1 = navLinks
    stripe2 = fontAcryl
    stripe3 = headVorname
    stripe4 = Farben.objects.get(area="farbstrich_bildFarbe")

    bild = Bilder.objects.get(area="Startseite-Hauptbild")
    context = {
    "homeBild" : bild.image,
    "farbeHintergrund" : hintergrund.farbcode,
    "farbeIntro" : fontAcryl.farbcode,
    "farbeHeadVorname" : headVorname.farbcode,
    "farbeHeadNachnameOverlay" : hintergrund.farbcode,
    "farbeHeadNachname" : headNachname2.farbcode,
    "farbeNavLinks" : navLinks.farbcode,
    "farbeStripe1" : stripe1.farbcode,
    "farbeStripe2" : stripe2.farbcode,
    "farbeStripe3" : stripe3.farbcode,
    "farbeStripe4" : stripe4.farbcode,
    }
    return context

def index(request):
    context = variables()
    navLinks = Farben.objects.get(area="Navbar_Verlinkungen")
    #image = Image.open(bild.image)
    #height = image.height
    #width = image.width

    #height = str(height)

    #b = Bilder.objects.all()
    #b = Bilder.objects.get(area = "header2")
    
#    print(connection.queries)
#    print( "b")
#    print(b)
#    cssFile = open("./website/static/website/bild.css", "w")
#    cssFile.write("header{height:"+height+"px;}")
    return render(request, 'index.html', context)
    

def delete(request, delete_id):
    context = { "delete_id" : "none"}
    if delete_id != "none":
        b = Bilder.objects.get(area = delete_id)
        b.delete()

    print("delete_id")
    print(delete_id)

    return render(request, 'index.html', context)
def about(request):
    context = variables()
    return render(request, 'about.html', context)
def galerie(request):

    bild = Bilder.objects.get(area="galerie")

    context = {
        "bild": bild.image,
    }

    return render(request, 'galerie.html', context)