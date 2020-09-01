from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'pages/index.html')



def loginUser(request):
    return render(request, 'pages/connect.html')


def registerUser(request):
    return render(request, 'pages/inscription.html')