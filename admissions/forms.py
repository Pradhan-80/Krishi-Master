from .models import ApplyInstitute
from django import forms


class instituteForm(forms.ModelForm):
    class Meta:
        model = ApplyInstitute
        fields = ('title','name', 'city','phone','email' )