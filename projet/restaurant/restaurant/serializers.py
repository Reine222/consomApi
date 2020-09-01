from resto.models import *
from rest_framework import serializers


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'


class PlatSerializer(serializers.ModelSerializer):
    catPlat = CategorieSerializer(many=True, required=False)

    class Meta:
        model = Plat
        fields = '__all__'


class TestimonySerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Testimony
        fields = '__all__'