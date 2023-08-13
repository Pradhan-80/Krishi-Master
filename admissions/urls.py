
from django.urls import include, path

from . import views

app_name = "admissions"
urlpatterns = [

    path("institutes/", views.list_View, name="institutes"),
    path("applyinstitutes/", views.SaveInstituteapply, name="applyinstitutes"),
   
   
    path("<slug:slug>/", views.institute_detail.as_view(), name="institute_details"  ),
    
]