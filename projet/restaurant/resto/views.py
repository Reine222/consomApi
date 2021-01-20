from django.shortcuts import render
from .models import Voir

# Create your views here.


def home(request, lang):
    translate =  Voir.objects.language(lang).all()
    data = {
        'translate': translate,
    }
    return render(request, 'pages/index.html', data)



def loginUser(request):
    return render(request, 'pages/connect.html')


def registerUser(request):
    return render(request, 'pages/inscription.html')