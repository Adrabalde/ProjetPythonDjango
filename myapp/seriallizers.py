from rest_framework import serializers
from .models import Individu


class IndividuSerializer(serializers.ModelSerializer) : 
    class Meta:
        model= Individu
        fields=['nom','prenom','email'] 