from django.contrib import admin
from .models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('question',)}


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
