from rest_framework import serializers

from api.models import Jeu

class JeuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jeu
        fields = '__all__'