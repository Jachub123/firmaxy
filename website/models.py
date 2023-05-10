from django.db import models

# Create your models here.

class Bilder(models.Model):
    area = models.CharField(max_length = 20, primary_key=True, verbose_name="area")
    image = models.ImageField(null=False, blank=False, upload_to="images/", verbose_name="image")
    height = models.IntegerField(null=False, blank=False, verbose_name="height")
    width = models.IntegerField(null=True, blank=False, verbose_name="width")
    
    class Meta:
        verbose_name = "Bild"
        verbose_name_plural = "Bilder"

    def __str__(self):
        return self.area