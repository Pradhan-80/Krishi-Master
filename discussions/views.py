from django.shortcuts import render,get_object_or_404,redirect
from .models import Question, Answer
from .forms import AnswerForm, QuestionForm
from django.contrib.auth.models import User

from django.contrib.auth import (
            authenticate,
            logout ,
            login
        )
from django.contrib import messages

def home(request):
    context = {}
    context['questions'] = Question.objects.all()
    return render(request, 'main/home.html', context)

def question_detail(request, slug):
    context = {}
    query =   Question.objects.filter(slug__iexact=slug)
    answers = Answer.objects.filter(question = query[0].id)
    context['object'] = query[0]
    context['answer_list'] = answers
    
    return render(request, "main/q_detail.html",context)



def create_answer(request, slug):
    context = {}
    q_obj = get_object_or_404(Question, slug=slug)
    if request.method=='POST':
        form = AnswerForm(request.POST)
        if form.is_valid():

            f = form.save(commit=False)
            f.author = request.user
            f.question = q_obj
            f.save()
            return redirect(q_obj.get_absolute_url())
        else:
            print("Invalid input")
    else:
        form = AnswerForm()
    context['form'] = form
    return render(request, "main/answerform.html", context)


def create_question(request):
    context = {}
    if request.method=='POST':
        form = QuestionForm(request.POST)
        if form.is_valid():

            f = form.save(commit=False)
            f.author = request.user
            f.save()
            return redirect("/discussions/home/")
        else:
            print("Invalid input")
    else:
        form = QuestionForm()
    context['form'] = form
    return render(request, "main/questionform.html", context)







from django.http import JsonResponse
from django.views.decorators.http import require_POST

from django.http import HttpResponseBadRequest


def ajax_required(f):


   def wrap(request, *args, **kwargs):
       if not request.is_ajax():
           return HttpResponseBadRequest()
       return f(request, *args, **kwargs)

   wrap.__doc__=f.__doc__
   wrap.__name__=f.__name__
   return wrap



def delete_question(request, slug):
    obj = Question.objects.get(slug__iexact=slug)
    obj.delete()
    messages.success(request,"{} deleted successfully".format(slug))
    return redirect("home")
def delete_answer(request, slug, author):
    question = Question.objects.get(slug__iexact=slug)
    ans_obj = Answer.objects.get(question=question, author=author)
    ans_obj.delete()
    messages.success(request,"Answer deleted successfully")
    return redirect(question.get_absolute_url())