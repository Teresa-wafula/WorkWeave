from django.shortcuts import render, redirect, get_object_or_404
from Jobs.models import Job, Application, Userprofile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from Jobs.forms import AddJobForm, ApplicationForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# def login_view(request):
#     user = request.user
#     if request.POST:
#         form = AccountAuthenticationForm(request.POST)
#         if form.is_valid:
#             form.save()


def home(request):
    jobs = Job.objects.all()
    return render(request, 'home.html', {'jobs':jobs})

def index(request):
    return render(request, 'index.html')

def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    return render(request, 'job_details.html', {'job': job})



# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#
#         if form.is_valid():
#             user = form.save()
#
#             account_type = request.POST.get('account_type', 'applicant')
#
#             if account_type == 'applicant':
#                 userprofile = Userprofile.objects.create(user=user, is_employer=True)
#                 userprofile.save()
                # login(request, user)
    #
    #
    #         else:
    #
    #             userprofile = Userprofile.objects.create(user=user)
    #             userprofile.save()
    #
    #             login(request, user)
    #
    #
    #             return redirect('login')
    #
    #
    # else:
    #     form = UserCreationForm()
    #     return render(request, 'register.html', {'form':form})


# @login_required
# def dashboard(request):
#     return render(request, 'dashboard.html')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            account_type = request.POST.get('account_type', 'applicant')

            if account_type == 'employer':
                userprofile = Userprofile.objects.create(user=user, is_employer=True)
                userprofile.save()
            else:
                userprofile = Userprofile.objects.create(user=user)
                userprofile.save()

            login(request, user)

            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})
@login_required
def applicant_dashboard(request):
    return render(request, 'applicant_dashboard.html')

@login_required
def emp_dashboard(request):
    return render(request, 'employer-dashboard.html')
@login_required
def add_job(request):
    if request.method =="POST":
        form = AddJobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by= request.user
            job.save()

            return redirect('dashboard')

    else:
        form = AddJobForm()
        return render(request, 'add_job.html', {'form':form})

@login_required
def apply(request, job_id):
    job = Job.objects.get(pk=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.created_by = request.user
            application.save()

            return redirect('dashboard')
    else:
        form = ApplicationForm()

    return render(request, 'applyjob.html', {'form': form, 'job': job})

@login_required
def view_application(request, application_id):
    #
    if request.user.userprofile.is_employer:
        application = get_object_or_404(Application, pk=application_id, job__created_by=request.user)
        context={
            'application':application

        }



    else:
        application = get_object_or_404(Application, pk = application_id, created_by = request.user)
        context={
            'application':application

        }
        return render(request, 'view_application.html', context)
@login_required
def view_job(request, job_id):
    job = get_object_or_404(Job, pk= job_id, created_by=request.user)
    return render(request, 'view_job.html', {'job':job})
