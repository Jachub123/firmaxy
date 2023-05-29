from django.shortcuts import render
from .models import *
from PIL import Image
from PIL.ExifTags import TAGS

# Create your views here.

def variables():
    hintergrund = Farben.objects.get(area="Hintergrund")
    fontAcryl = Farben.objects.get(area="Head1_Schrift_Acryl")
    headVorname = Farben.objects.get(area="Head2_Schrift_Evita")
    headNachname = Farben.objects.get(area="Head4_Schrift_Nonne")
    headNachname2 = Farben.objects.get(area="Head4_Schrift_Nonne2")
    navLinks = Farben.objects.get(area="Navbar_Verlinkungen")
    navLinksGradient1 = Farben.objects.get(area="Farbverlauf_Farbe1")
    navLinksGradient2 = Farben.objects.get(area="Farbverlauf_Farbe2")
    stripe1 = navLinks
    stripe2 = fontAcryl
    stripe3 = headVorname
    stripe4 = Farben.objects.get(area="farbstrich_bildFarbe")

    HomeBild = BilderFestlegen.objects.get(area="HP")
    AboutMebild = BilderFestlegen.objects.get(area="AM")
    context = {
    "colorVars" :":root{ --colorTextgrad1: #"+headVorname.farbcode+"; --colorTextgrad2: #"+stripe4.farbcode+"; --initialLinkColor: #"+navLinks.farbcode+";}",
    
    "homeBild" : HomeBild.image,
    "AboutMebild" : AboutMebild.image,
    "farbeHintergrund" : "#"+hintergrund.farbcode,
    "farbeIntro" : "#"+fontAcryl.farbcode,
    "farbeHeadVorname" : "#"+headVorname.farbcode,
    "farbeHeadNachnameOverlay" : "#"+hintergrund.farbcode,
    "farbeHeadNachnameOben" : "#"+headNachname.farbcode,
    "farbeHeadNachname" : "#"+headNachname2.farbcode,
    "farbeNavLinks" : "#"+navLinks.farbcode,
    "farbeNavLinksGradient1" : "#"+navLinksGradient1.farbcode,
    "farbeNavLinksGradient2" : "#"+navLinksGradient2.farbcode,
    "farbeStripe1" : "#"+stripe1.farbcode,
    "farbeStripe2" : "#"+stripe2.farbcode,
    "farbeStripe3" : "#"+stripe3.farbcode,
    "farbeStripe4" : "#"+stripe4.farbcode,
    }
    return context

def index(request):
    
    context = variables()
    context["HeadTextClass"] = "HomeHeadText"
    context["HeadImgClass"] = "homeImg"
    context["home"] = True
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
        b = BilderFestlegen.objects.get(area = delete_id)
        b.delete()

    print("delete_id")
    print(delete_id)

    return render(request, 'index.html', context)
def about(request):
    CV1 = Texte.objects.get(textfeld="Lebenslauf-Station1")
    headline = []
    text = []
    CV1 = CV1.text.split("\n")
    for index, wort in enumerate(CV1):
        if index % 2 == 0:
            headline.append(wort)
        else:
            text.append(wort)
    print("headline")
    print(headline)
    print("text")
    print(text)
    context = variables()
    context["CV1Head"] = headline
    context["CV1"] = text
    context["HeadTextClass"] = "AboutHeadText"
    context["HeadImgClass"] = "AboutHeadImg"
    context["about"] = True
    return render(request, 'about.html', context)
def galerie(request):

    bild = BilderFestlegen.objects.get(area="galerie")

    context = {
        "bild": bild.image,
    }

    return render(request, 'galerie.html', context)