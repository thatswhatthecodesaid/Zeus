from django import forms
from .models import *

class AcForm(forms.ModelForm):
    class Meta:
        model = Ac
        fields = "__all__"

class AcIot(forms.Form):
    ac_io = forms.BooleanField(required=False)
    ac_temp = forms.CharField(max_length=100)
    