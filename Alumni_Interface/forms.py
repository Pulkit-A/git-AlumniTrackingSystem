from django import forms
from django.contrib.auth.models import User
from .models import AlumniInfo


class AlumniForm(forms.ModelForm):
    class Meta:
        model = AlumniInfo
        fields = [
            'name', 'r_no', 'email', 'course', 'm_no', 'org_name', 'org_add', 'al_dsg', 'profile_pic',
        ]


class EditForm(forms.ModelForm):
    class Meta:
        model = AlumniInfo
        fields = [
            'email', 'course', 'm_no', 'org_name', 'org_add', 'al_dsg', 'profile_pic',
        ]