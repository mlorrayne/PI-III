from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import Voluntariado, Apoio, Transparencia, Gasto
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .forms import ApoioForm, VoluntariadoForm

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
            return redirect('apoio_agradecimento')  # Corrigi a ordem das redireções
    else:
        form = ApoioForm()
    return render(request, 'core/apoio.html', {'form': form})

def voluntariado(request):
    if request.method == 'POST':
        form = VoluntariadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('voluntariado_sucesso')  # Corrigi a ordem das redireções
    else:
        form = VoluntariadoForm()
    return render(request, 'core/voluntariado.html', {'form': form})

def voluntariado_sucesso(request):
    return render(request, 'core/voluntariado_sucesso.html')

def apoio_agradecimento(request):
    return render(request, 'core/apoio_agradecimento.html')

@staff_member_required
def lista_voluntariados(request):
    voluntarios_list = Voluntariado.objects.order_by("nome")
    paginator = Paginator(voluntarios_list, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/lista_voluntariados.html', {"page_obj": page_obj})

@staff_member_required
def lista_apoios(request):
    apoios_list = Apoio.objects.order_by("nome")
    paginator = Paginator(apoios_list, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/lista_apoios.html', {"page_obj": page_obj})

@staff_member_required
def editar_voluntariado(request, pk):
    voluntariado = get_object_or_404(Voluntariado, pk=pk)
    if request.method == 'POST':
        form = VoluntariadoForm(request.POST, instance=voluntariado)
        if form.is_valid():
            form.save()
            return redirect('lista_voluntariados')
    else:
        form = VoluntariadoForm(instance=voluntariado)
    # Passa uma string simples 'Voluntariado' para o template ao invés de __class__.__name__
    return render(request, 'core/editar_voluntariado.html', {'form': form, 'tipo': 'Voluntariado'})

@staff_member_required
def excluir_voluntariado(request, pk):
    voluntariado = get_object_or_404(Voluntariado, pk=pk)
    if request.method == 'POST':
        voluntariado.delete()
        return redirect('lista_voluntariados')
    return render(request, 'core/confirma_exclusao.html', {'obj': voluntariado, 'tipo': 'Voluntariado'})

@staff_member_required
def editar_apoio(request, pk):
    apoio = get_object_or_404(Apoio, pk=pk)
    if request.method == 'POST':
        form = ApoioForm(request.POST, instance=apoio)
        if form.is_valid():
            form.save()
            return redirect('lista_apoios')
    else:
        form = ApoioForm(instance=apoio)
    # Passa uma string simples 'Apoio' para o template
    return render(request, 'core/editar_apoio.html', {'form': form, 'tipo': 'Apoio'})

@staff_member_required
def excluir_apoio(request, pk):
    apoio = get_object_or_404(Apoio, pk=pk)
    if request.method == 'POST':
        apoio.delete()
        return redirect('lista_apoios')
    return render(request, 'core/confirma_exclusao.html', {'obj': apoio, 'tipo': 'Apoio'})

def transparencia(request):
    transparencia, created = Transparencia.objects.get_or_create(id=1)
    relatorio_gastos = Gasto.objects.all()

    return render(request, "core/transparencia.html", {
        "ano_anterior": transparencia.ano_anterior,
        "ano_atual": transparencia.ano_atual,
        "meta_doacoes": transparencia.meta_doacoes,
        "relatorio_gastos": relatorio_gastos
    })

@login_required
def editar_transparencia(request):
    transparencia = Transparencia.objects.get(id=1)
    relatorio_gastos = Gasto.objects.all()

    if request.method == "POST":
        transparencia.ano_anterior = request.POST.get("ano_anterior")
        transparencia.ano_atual = request.POST.get("ano_atual")
        transparencia.meta_doacoes = request.POST.get("meta_doacoes")
        transparencia.save()

        for gasto in relatorio_gastos:
            gasto.valor = request.POST.get(f"gasto_{gasto.id}")
            gasto.save()

        return redirect("transparencia")
    
    return render(request, "core/editar_transparencia.html", {
        "transparencia": transparencia,
        "relatorio_gastos": relatorio_gastos
    })


