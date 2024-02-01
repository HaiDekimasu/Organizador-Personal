from django.shortcuts import render, redirect
from .models import Lista
from .forms import ListaForm
from django.contrib import messages

# Create your views here.
def index(request):

    listas = Lista.objects.filter(title__contains=request.GET.get('Buscar', ''))
    context = {
        'listas': listas
    }
    return render(request, 'lista/index.html', context)
    
def view(request, id):
    lista = Lista.objects.get(id=id)
    
    context = {
        'lista': lista
    }
    return render(request, 'lista/detail.html', context)

def edit(request, id):
    lista = Lista.objects.get(id=id)
    
    if (request.method == 'GET'):
        form = ListaForm(instance = lista)
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'lista/edit.html', context)
    
    if(request.method == 'POST'):
        form = ListaForm(request.POST, instance= lista)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
            'id': id,
        }
        messages.success(request, ' Tarea Actualizada')
        return render(request, 'lista/edit.html', context)
    
def create(request):
    if(request.method == 'GET'):
        form = ListaForm()
        context = {
            'form': form,
        }
        return render(request, 'lista/create.html', context)
    
    if request.method == 'POST':
        form = ListaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('lista')


def delete(request, id):
    lista = Lista.objects.get(id=id)
    lista.delete()
    return redirect('lista')