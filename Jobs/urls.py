
from django.urls import path
from django.contrib.auth import views
from Jobs.views import home, register,index,job_detail,apply,view_application,view_job,applicant_dashboard,add_job,emp_dashboard


urlpatterns = [
    path('login/',views.LoginView.as_view(template_name='login.html'), name='login'),
    path('home/',home, name="home"),
    path('register/', register, name="register"),
    path('', index, name="index"),
    path('jobdetails/<int:job_id>/', job_detail, name="jobdetails"),
    path('applyjob/<int:job_id>/',apply, name="applyjob"),
    path('application/<int:application_id>/', view_application, name="application"),
    path('job/<int:job_id>/', view_job, name="job"),
    path('dashboard/',applicant_dashboard, name="dashboard"),
    path('emp_dashboard/',emp_dashboard, name="emp_dashboard"),
    path('add_job/', add_job, name="add_job"),

]
