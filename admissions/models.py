from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField



STATUS = ((0, "Draft"), (1, "Publish"))


class InstitutesListing(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
  
    featured = models.URLField()
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("institute_detail", kwargs={"slug": str(self.slug)})
    


class ApplyInstitute(models.Model):
    title = models.ForeignKey(InstitutesListing,on_delete=models.CASCADE,related_name='applyinstitute')
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField()

def __str__(self):
        return self.name




