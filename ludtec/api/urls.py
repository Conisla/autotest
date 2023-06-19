from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import JeuViewset

jeu = DefaultRouter()
jeu.register('jeu', JeuViewset, basename= 'Jeu')
urlpatterns = [
    path('', include(jeu.urls)),
]