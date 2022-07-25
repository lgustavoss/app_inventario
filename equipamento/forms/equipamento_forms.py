from django import forms
from django.forms import DateInput
from tipo_equipamento.models import TipoEquipamento

from colaborador.models import Colaborador
from ..models import Equipamento


class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = '__all__'
        widgets = {
            'data': DateInput(
                attrs={'type': "date"}
            )
        }
