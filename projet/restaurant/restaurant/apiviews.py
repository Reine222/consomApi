from rest_framework import viewsets
from resto.models import *
from .serializers import CategorieSerializer, PlatSerializer, TestimonySerializer


class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    
class PlatViewSet(viewsets.ModelViewSet):
    queryset = Plat.objects.all()
    serializer_class = PlatSerializer
    
class TestimonyViewSet(viewsets.ModelViewSet):
    queryset = Testimony.objects.all()
    serializer_class = TestimonySerializer