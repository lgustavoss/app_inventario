from django import forms
from localflavor.br.forms import BRCNPJField
from ..models import Empresa
from django.forms.utils import ErrorList


class EmpresaForm(forms.ModelForm):
    cnpj = BRCNPJField()

    class Meta:
        model = Empresa
        fields = '__all__'