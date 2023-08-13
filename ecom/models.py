from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField



STATUS = ((0, "Draft"), (1, "Publish"))


class ProductListing(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
  
    featured = models.ImageField(upload_to='static/images/')
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("product_detail", kwargs={"slug": str(self.slug)})



class buyproduct(models.Model):
    product = models.ForeignKey(ProductListing, on_delete=models.CASCADE, related_name="productbuyer",null=True, blank=True,)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)