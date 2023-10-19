from django.shortcuts import render

def index(request):
    return render(request,'templatesApp/index.html')


def Argentina(request):
    data={
        "titulo": "Titulos",
        'Copa Mundial':"",
        'Copa America':"",
        'Copa Conmebol-UEFA':"",
        'Copa Confederacion':"",
        'imagen':'imagenes/Arg.png'
    }
    return render(request,'templatesApp/Paises.html')

def Brasil(request):
    data={
        "titulo": "Titulos",
        'Copa Mundial':"",
        'Copa America':"",
        'Copa Conmebol-UEFA':"",
        'Copa Confederacion':"",
        'imagen':'imagenes/Bra.webp'
        
    }
    return render(request,'templatesApp/Paises.html')

def Uruguay(request):
    data={
        "titulo": "Titulos",
        'Copa Mundial':"",
        'Copa America':"",
        'Copa Conmebol-UEFA':"",
        'Copa Confederacion':"",
        'imagen':'imagenes/uru.jpg'
        
    }
    return render(request,'templatesApp/Paises.html')

# Create your views here.
