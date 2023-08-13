from django.db import models
from django.contrib.auth.models import User
from django.utils.text  import slugify
from django.conf import settings



Question_GENRE_CHOICES = (
    ("A", "agriculture"),
    ("F", "Farm"),
    ("O", "Organic"),
    ("S", "Soil"),
    ("P", "Pest"),
    ("S", "Study"),
    ("N", "Animals"),
)

class Question(models.Model):
    author    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    genre     = models.CharField(choices = Question_GENRE_CHOICES, max_length=1)
    question  = models.TextField()
    created   = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated   = models.DateTimeField(auto_now=True, auto_now_add=False)
    slug      = models.SlugField()
    question_like = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="question_liked_by")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.question)
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('q_detail', args=[str(self.slug)])

class Answer(models.Model):
    author    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    answer    = models.TextField(help_text="Enter your answer here !!!")
    question  = models.ForeignKey(Question, on_delete=models.CASCADE)
    created   = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated   = models.DateTimeField(auto_now=True,     auto_now_add=False)
    answer_like = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="answer_liked_by")

    def __str__(self):
        return self.answer