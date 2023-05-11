from django.shortcuts import render
from .models import *
from PIL import Image
from PIL.ExifTags import TAGS
from django.conf import settings
from django.db import connection

# Create your views here.
def index(request):
    bild = Bilder.objects.get(area="header2")
    image = Image.open(bild.image)
    height = image.height
    height = str(height)

    c = Bilder.objects.all()
    b = Bilder.objects.filter(width = "200")
    print(connection.queries)
    cssFile = open("./website/static/website/bild.css", "w")
    cssFile.write("header{height:"+height+"px;}")
    context = {
        "bild" : bild.image,
        "height" : height,
        "b" : b,
    }
    return render(request, 'index.html', context)
def about(request):
    return render(request, 'about.html', {})
def galerie(request):

    bild = Bilder.objects.get(area="galerie")

    context = {
        "bild": bild.image,
    }

    return render(request, 'galerie.html', context)