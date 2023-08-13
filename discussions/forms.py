from django import forms
from discussions.models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate






   



class QuestionForm(forms.ModelForm):
    class Meta:

        model = Question
        fields = ['question', 'genre']

class EditQuestionForm(forms.ModelForm):
    class Meta:

        model = Question
        fields = ['question', 'genre']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('answer',)




# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields= ['bio','profession', ]