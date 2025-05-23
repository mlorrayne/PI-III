from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def historia(request):
    return render(request, 'core/historia.html')

def contato(request):
    return render(request, 'core/contato.html')

