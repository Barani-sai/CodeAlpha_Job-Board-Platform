from django import forms
from .models import Job, Applicant

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'company', 'location', 'salary']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['resume']
