from django.urls import path
from accounts import views

app_name = "account"

urlpatterns = [

    path('student/register/', views.student_registration, name='student-registration'),
    path('recruiter/register/', views.recruiter_registration, name='recruiter-registration'),
    path('profile/edit/<int:id>/', views.student_edit_profile, name='edit-profile'),
    path('login/', views.user_logIn, name='login'),
    path('logout/', views.user_logOut, name='logout'),
]