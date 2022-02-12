from django import forms
from .models import Formation

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = "__all__"

class RechercheForm(forms.Form):
    subject = forms.CharField(required=False)

