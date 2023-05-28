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
    
class Galerie(models.Model):
    name = models.CharField(max_length = 20, verbose_name="Bildname", primary_key=True)
    image = models.ImageField(null=False, verbose_name="Bild", upload_to="images/galerie")
    höhe = models.IntegerField(verbose_name="Höhe")
    breite = models.IntegerField(verbose_name="Breite")

    class Meta:
        verbose_name = "Galerie"
        verbose_name_plural = "Galerie-Bilder"

    def __str__(self):
        return self.name