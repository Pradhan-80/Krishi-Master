from django.urls import path
from jobportal import views

app_name = "jobportal"


urlpatterns = [

    path('', views.home_view, name='home'),
    path('planform/', views.form_view, name='planform'),
    path('planformstudent/', views.formstudent_view, name='planformstudent'),
    path('jobs/', views.job_list_View, name='job-list'),
    path('job/create/', views.create_job_View, name='create-job'),
    path('job/<int:id>/', views.single_job_view, name='single-job'),
    path('apply-job/<int:id>/', views.apply_job_view, name='apply-job'),
    path('bookmark-job/<int:id>/', views.job_bookmark_view, name='bookmark-job'),
    path('about/', views.single_job_view, name='about'),
    path('contact/', views.single_job_view, name='contact'),
    path('result/', views.search_result_view, name='search_result'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/recruiter/job/<int:id>/applicants/', views.all_applicants_view, name='applicants'),
    path('dashboard/recruiter/job/edit/<int:id>', views.job_edit_view, name='edit-job'),
    path('dashboard/recruiter/applicant/<int:id>/', views.applicant_details_view, name='applicant-details'),
    path('dashboard/recruiter/close/<int:id>/', views.make_complete_job_view, name='complete'),
    path('dashboard/recruiter/delete/<int:id>/', views.delete_job_view, name='delete'),
    path('dashboard/student/delete-bookmark/<int:id>/', views.delete_bookmark_view, name='delete-bookmark'),


]