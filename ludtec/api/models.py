from django.db import models

# Create your models here.

class Jeu(models.Model):
    id_jeu = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50,blank=True, null=True)