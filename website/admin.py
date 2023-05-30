from django.contrib import admin
from .models import *
from django import forms
from django.core.exceptions import ValidationError

# Register your models here.


class FarbenAdmin(admin.ModelAdmin):
    list_display = ("area","farbcode",)
admin.site.register(Farben, FarbenAdmin)
admin.site.register(Texte)

class MyModelAdminForm(forms.ModelForm):
    class Meta:
        model = BilderFestlegen
        fields = ('name', 'area', 'image', 'width', 'height')

class BilderAdmin(admin.ModelAdmin):
    list_display = ("name","area",)
    ordering = ("name",)
    search_fields = ("area", "name",)
    class Media:
        js = ('js/admin_field_visibility.js',)
    def get_fields(self, request, obj=None):
        form = MyModelAdminForm
        fields = list(super().get_fields(request, obj))

        # Determine the selected option value
        selected_option = request.POST.get('area') if request.method == 'POST' else (obj.area if obj else None)

        # Conditionally modify the fields list based on the selected option
        if selected_option == 'G':
            
            if request.POST.get('width') == "" or request.POST.get('height') == "":
                raise ValidationError("Höhe und Breite EINGEBE!")

        return fields 
admin.site.register(BilderFestlegen, BilderAdmin)