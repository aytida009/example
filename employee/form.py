from django import forms
from.models import Employe

class EmpForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields= "__all__"
    