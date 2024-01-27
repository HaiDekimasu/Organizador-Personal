from django.shortcuts import render, redirect
from .models import Contactos
from .forms import ContactosForm
from django.contrib import messages

    # Create your views here.
def index(request):
    contacto = Contactos.objects.filter(name__contains=request.GET.get('Buscar', ''))

    context = {
        'contacto': contacto
    }
    return render(request, 'contactos/index.html', context)


def view(request, id):
    contactos = Contactos.objects.get(id=id)

    context = {
        'contactos': contactos
    }
    return render(request, 'contactos/detail.html', context)

def edit(request, id):
    contactos = Contactos.objects.get(id=id)

    if (request.method == 'GET'):
        form = ContactosForm(instance = contactos)
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'contactos/edit.html', context)

    if(request.method == 'POST'):
        form = ContactosForm(request.POST, instance= contactos)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
            'id': id,
        }
        messages.success(request, 'Contacto Actualizado')
        return render(request, 'contactos/edit.html', context)

def create(request):
    if(request.method == 'GET'):
        form = ContactosForm()
        context = {
            'form': form,
        }
        return render(request, 'contactos/create.html', context)

    if request.method == 'POST':
        form = ContactosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('contactos')

def delete(request, id):
    contactos = Contactos.objects.get(id=id)
    contactos.delete()
    return redirect('contactos')