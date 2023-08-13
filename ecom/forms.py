from django import forms

from .models import buyproduct


class CommentForm(forms.ModelForm):
    class Meta:
        model = buyproduct
        fields = ("product","name", "email", "body")