from django import forms
from localflavor.br.forms import BRCPFField
from ..models import Colaborador


class ColaboradorForm(forms.ModelForm):
    cpf = BRCPFField()

    class Meta:
        model = Colaborador
        fields = '__all__'
