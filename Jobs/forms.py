from django import forms
from Jobs.models import Job, Application
from django.contrib.auth.forms import AuthenticationForm
from Jobs.models import User
# # Create your forms here.

class RegistrationForm(AuthenticationForm):
    class Meta:
        Model = User
        fields = ['username','is_employer','is_applicant','password1', 'password2']



class AddJobForm(forms.ModelForm):
    class Meta:
        model= Job
        fields = ['title', 'description', 'long_description']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['content', 'experience']

