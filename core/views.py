from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ApoioForm, VoluntariadoForm
from django.contrib.admin.views.decorators import staff_member_required
from .models import Voluntariado, Apoio

def index(request):
    return render(request, 'core/index.html')

def historia(request):
    return render(request, 'core/historia.html')

def contato(request):
    return render(request, 'core/contato.html')

def apoio(request):
    if request.method == 'POST':
        form = ApoioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('voluntariado_sucesso') 
    else:
        form = ApoioForm()
    return render(request, 'core/apoio.html', {'form': form})

def voluntariado(request):
    if request.method == 'POST':
        form = VoluntariadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('apoio_agradecimento')  
    else:
        form = VoluntariadoForm()
    return render(request, 'core/voluntariado.html', {'form': form})

def voluntariado_sucesso(request):
    return render(request, 'core/voluntariado_sucesso.html')

def apoio_agradecimento(request):
    return render(request, 'core/apoio_agradecimento.html')

@staff_member_required
def lista_voluntariados(request):
    voluntariados = Voluntariado.objects.all()
    return render(request, 'core/lista_voluntariados.html', {'voluntariados': voluntariados})

@staff_member_required
def lista_apoios(request):
    apoios = Apoio.objects.all()
    return render(request, 'core/lista_apoios.html', {'apoios': apoios})

