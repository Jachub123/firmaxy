from django.shortcuts import render
from .models import *
from PIL import Image
from PIL.ExifTags import TAGS

# Create your views here.
def index(request):
    bild = Bilder.objects.get(area="header2")
    image = Image.open("C:/Python/jachub/firmaxy/images/images/20230509_191744.jpg")
    breite = image.height
    context = {
        "bild" : bild,
        "breite" : breite,
    }
    return render(request, 'index.html', context)
def about(request):
    return render(request, 'about.html', {})
def galerie(request):
    return render(request, 'galerie.html', {})