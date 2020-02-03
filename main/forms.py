from django import forms
from .models import *

class Uform(forms.ModelForm):
    class Meta:
        model = U
        fields = "__all__"


class Change_data(forms.ModelForm):
    class Meta:
        model = U
        fields = ("score",)


class ac(forms.Form):
    on = forms.BooleanField(required=False)
    city = forms.CharField(max_length=100)
    ac_temp = forms.CharField(max_length=100)


class AppliancesForm(forms.ModelForm):
    
    class Meta:
        model = Appliances
        fields = "__all__"
        