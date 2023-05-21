from django.shortcuts import render
from .models import *
from PIL import Image
from PIL.ExifTags import TAGS
from django.views.generic import TemplateView

# Create your views here.
class Themes(TemplateView):
    template_name = 'static/website/style.css'
    content_type='text/css'
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['color'] = "red"
        return self.render_to_response(context)

""" def css(request):

    return render(request, 'index.html', context) """
def index(request):
    farbe = Farben.objects.get(area="Hintergrund")
    bild = Bilder.objects.get(area="Startseite-Hauptbild")
    image = Image.open(bild.image)
    height = image.height
    width = image.width
    #height = str(height)

    b = Bilder.objects.all()
    #b = Bilder.objects.get(area = "header2")
    
#    print(connection.queries)
#    print( "b")
#    print(b)
#    cssFile = open("./website/static/website/bild.css", "w")
#    cssFile.write("header{height:"+height+"px;}")
    context = {
        "homeBild" : bild.image,
        "farbe" : farbe.farbcode,
    }
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
    bild = Bilder.objects.get(area="about")
    context = {
        "bild": bild.image,
    }
    return render(request, 'about.html', context)
def galerie(request):

    bild = Bilder.objects.get(area="galerie")

    context = {
        "bild": bild.image,
    }

    return render(request, 'galerie.html', context)