from django.db import models

# Create your models here.

class BilderFestlegen(models.Model):

    bildArea =[ 
        ("HP", "Startseiten-Bilder"),
        ("AM", "Übermich-Bilder"),
        ("G", "Galerie-Bilder"),
    ]

    name = models.CharField(max_length = 20, primary_key=True, verbose_name="name")
    area = models.CharField(max_length = 20, choices=bildArea, verbose_name="area")
    image = models.ImageField(null=False, blank=False, upload_to="images/", verbose_name="image")
    width = models.IntegerField(null=True, blank=True, verbose_name="width")
    height = models.IntegerField(null=True, blank=True, verbose_name="height")

    class Meta:
        verbose_name = "Bild"
        verbose_name_plural = "Bilder"

    def __str__(self):
        return self.name
    
class Farben(models.Model):
    area = models.CharField(max_length = 20, verbose_name="area", primary_key=True)
    farbcode = models.CharField(max_length = 20, verbose_name="farbcode")
    
    class Meta:
        verbose_name = "Farbe"
        verbose_name_plural = "Farben"

    def __str__(self):
        return self.area
    
class Texte(models.Model):
    textfeld = models.CharField(max_length = 25, verbose_name="text-Feld", primary_key=True)
    text = models.TextField(max_length = 1000, verbose_name="text")
    
    class Meta:
        verbose_name = "Text"
        verbose_name_plural = "Texte"

    def __str__(self):
        return self.textfeld