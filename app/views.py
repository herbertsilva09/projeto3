from django.shortcuts import render

def x(request):
    return render(request,'pagina_inicial.html')

def c(request):
    return render(request,'pagina2.html' )

def l(request):
    return render(request,'pagina3.html')

def condicionais(request):
    return render(request,'pagina4.html')

def funcoes(request):
    return render(request,'pagina5.html')

def modulo(request):
    return render(request,'pagina6.html')

def classes(request):
    return render(request,'pagina7.html')

# Create your views here.
