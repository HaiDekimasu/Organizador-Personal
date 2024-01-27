from django.forms import ModelForm
from .models import Contactos

class ContactosForm(ModelForm):
    class Meta:
        model = Contactos
        exclude = ('date',)