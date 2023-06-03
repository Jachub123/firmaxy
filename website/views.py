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
    
def textmaker(dbText):
    headline = []
    text = []
    dbText = dbText.split("\n")
    for index, wort in enumerate(dbText):
        if index % 2 == 0:
            headline.append(wort)
        else:
            text.append(wort)
    return zip(headline, text)

def index(request):
    h1 = Texte.objects.get(textfeld="Startseite-Überschrift")
    homeText = Texte.objects.get(textfeld="Startseite-Text")
    
    context = variables()
    context["HeadTextClass"] = "HomeHeadText"
    context["HeadImgClass"] = "homeImg"
    context["h1"] = h1.text
    context["text"] = textmaker(homeText.text)
    context["home"] = True
    
    
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
    CV1 = Texte.objects.get(textfeld="Übermich-Text")
    
    aboutText = textmaker(CV1.text)
    context = variables()
    context["aboutText"] = aboutText
    context["HeadTextClass"] = "AboutHeadText"
    context["HeadImgClass"] = "AboutHeadImg"
    context["about"] = True
    return render(request, 'about.html', context)
def galerie(request):
    bilder = BilderFestlegen.objects.filter(area="Galerie-Bilder")
    context = variables()
    height = []
    width = []

    for bild in bilder:
        image = Image.open(bild.image)
        height.append(str(image.height))
        width.append(str(image.width))
        print(bild.image)
    bilderUndMase = zip(bilder, height, width)
    
    """  b = Bilder.objects.all()
    b = Bilder.objects.get(area = "header2") """
    

    context["bilder"] = bilder
    context["bilderUndMase"] = bilderUndMase
    context["HeadTextClass"] = "AboutHeadText"
    context["imgHeight"] = height
    context["imgWidth"] = width
    context["galerie"] = True

    return render(request, 'galerie.html', context)

def singlePicView(request, name):
    print(f"LOOOOOOOOOL: {request.GET.get('wohn','')}")
    bild = BilderFestlegen.objects.get(name=name)
    background = BilderFestlegen.objects.get(name="WohnzimmerBild")
    
    context = variables()
    context["bildName"] = bild.name
    context["bildWidth"] = bild.width
    context["bildHeight"] = bild.height
    context["bildDesc"] = bild.desc

    if request.GET.get('wohn','') == "true":
        bildSize = Image.open(bild.image)
        if bildSize.height > bildSize.width:
            context["widthOrHeight"] = "height"
        else:
            context["widthOrHeight"] = "width"
        context["bild"] = background
        context["wandBild"] = bild.image
        context["jumpTo"] = {                            
                            "target": "last",
                            "class": "last",
                             "bild" : bild.name+"#scroll"
                             }
        
    else:
        context["bild"] = bild
        context["jumpTo"] = {                            
                            "target": "next",
                            "bild": "?wohn=true#scroll"
                            }

    context["HeadTextClass"] = "singlePicHead"
    context["HeadImgClass"] = "singlePic"

    return render(request, 'einzelBild.html', context)