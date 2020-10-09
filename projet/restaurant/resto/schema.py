import graphene
from .models import *
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField




class CategorieNode(DjangoObjectType):
    class Meta:
        model = Categorie
        filter_fields = ['nom', 'catPlat', 'date_add', 'date_upd', 'status']
        interfaces = (relay.Node, )


class PlatNode(DjangoObjectType):
    class Meta:
        model = Plat
        # Allow for some more advanced filtering here
        filter_fields = {
            'image': [],
            'nom': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
            'categorie': ['exact'],
            'categorie__id': ['exact'],
            'prix':  ['exact', 'icontains'],
            
            'date_add': ['exact', 'icontains', 'istartswith'],
            'date_upd': ['exact', 'icontains', 'istartswith'],
            'status': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class TestimonyNode(DjangoObjectType):
    class Meta:
        model = Testimony
        filter_fields = {
            'image': [],
            'nom': ['exact', 'icontains', 'istartswith'],
            'profession': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
            'fb': ['exact', 'icontains', 'istartswith'],
            'tweet': ['exact', 'icontains', 'istartswith'],
            'instagram': ['exact', 'icontains', 'istartswith'],
            
            'date_add': ['exact', 'icontains', 'istartswith'],
            'date_upd': ['exact', 'icontains', 'istartswith'],
            'status': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )



class ServiceNode(DjangoObjectType):
    class Meta:
        model = Service
        filter_fields = ['titre', 'icon', 'description', 'date_add', 'date_upd', 'status']
        interfaces = (relay.Node, )



class Query(graphene.ObjectType):
    categorie = relay.Node.Field(CategorieNode)
    all_categories = DjangoFilterConnectionField(CategorieNode)

    plat = relay.Node.Field(PlatNode)
    all_plats = DjangoFilterConnectionField(PlatNode)

    testimony = relay.Node.Field(TestimonyNode)
    all_testimonys = DjangoFilterConnectionField(TestimonyNode)

    service = relay.Node.Field(ServiceNode)
    all_services = DjangoFilterConnectionField(ServiceNode)

    service = graphene.List(
        ServiceNode,
        first=graphene.Int(),
        skip=graphene.Int(),    
    )

    def resolve_links(self, info, search=None, first=None, skip=None, **kwargs):
        qs = Service.objects.all()

        if skip:
            qs = qs[skip:]

        if first:
            qs = qs[:first]

        return qs

