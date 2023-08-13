from django.urls import path
from discussions.views import (
    delete_answer,
    delete_question,
    home,
    question_detail,
    create_answer,
    create_question,
   
    )

app_name = "discussions"

urlpatterns = [

    path("home/", home, name="home"),
    path("answer/<slug>", create_answer, name="answer"),
    path("q_detail/<slug>/", question_detail, name="q_detail"),
    path("question/", create_question, name="question"),
   
    path("delete_question/<slug>", delete_question, name="delete_question"),
    path("delete_answer/<slug>/<author>", delete_answer, name="delete_answer"),


]