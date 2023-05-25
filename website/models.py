from django.db import models

# Create your models here.

class Bilder(models.Model):
    
    AREA = (
    ('galerie','GALERIE-BILD'),
    ('startseiten','STARTSEITEN-BILD'),
    ('über-mich','ÜBER-MICH-BILD'),
    )

    name = models.CharField(max_length = 20, verbose_name="name", primary_key=True)
    area = models.CharField(max_length = 14, choices=AREA, verbose_name="Bereich", default="galerie")
    height = models.IntegerField(null=True, blank=True, verbose_name="height")
    width = models.IntegerField(null=True, blank=True, verbose_name="width")
    image = models.ImageField(null=False, blank=False, upload_to="images/", verbose_name="Bild")
    
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