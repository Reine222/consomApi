from resto.models import *
from rest_framework import serializers

class TestimonySerializer(serializers.ModelSerializer):
       
    class Meta:
        model = Testimony
        fields = '__all__'

        
class PlatSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Plat
        fields = '__all__'
        depth = 1

class CategorieSerializer(serializers.ModelSerializer):
    catPlat = PlatSerializer(many=True, required=False)
    
    class Meta:
        model = Categorie
        fields = '__all__'




