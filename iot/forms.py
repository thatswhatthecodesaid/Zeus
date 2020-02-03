from django import forms
from .models import *
from main.models import *

class AcForm(forms.ModelForm):
    class Meta:
        model = Ac
        fields = "__all__"

class AcIot(forms.Form):
    ac_io = forms.BooleanField(required=False)
    ac_temp = forms.CharField(max_length=100)


class UsageForm(forms.ModelForm):
    start = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    stop = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    class Meta:
        model = Usage
        fields = "__all__"  