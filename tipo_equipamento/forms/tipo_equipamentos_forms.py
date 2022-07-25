from django import forms
from ..models import TipoEquipamento


class TipoEquipamentoForm(forms.ModelForm):
    class Meta:
        model = TipoEquipamento
        fields = '__all__'
