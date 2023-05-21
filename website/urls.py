from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('galerie', views.galerie, name='galerie'),
    path('delete/<str:delete_id>', views.delete, name='delete' ),
    path("static/website/style.css", views.Themes.as_view(), name='theme-variables'),
]