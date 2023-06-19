from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import JeuSerializer
from api.models import Jeu

# Create your views here.

class JeuViewset(viewsets.ModelViewSet):
    queryset = Jeu.objects.all()
    serializer_class = JeuSerializer