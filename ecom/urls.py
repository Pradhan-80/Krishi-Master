
from django.urls import include, path

from . import views
app_name = "ecom"

urlpatterns = [

    path("products/", views.list_View, name="products"),
   
    path("<slug:slug>/", views.product_detail, name="product_details"  ),
]