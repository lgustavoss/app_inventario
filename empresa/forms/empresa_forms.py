from django import forms
from ..models import Empresa
from django.forms.utils import ErrorList


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'