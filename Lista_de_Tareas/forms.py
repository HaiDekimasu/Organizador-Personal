from django.forms import ModelForm
from .models import Lista

class ListaForm(ModelForm):
    class Meta:
        model = Lista
        exclude = ('date',)