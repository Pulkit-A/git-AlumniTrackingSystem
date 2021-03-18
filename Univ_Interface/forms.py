from django import forms
from django.contrib.auth.models import User
from .models import UnivInfo, EventInfo


class UnivForm(forms.ModelForm):
    class Meta:
        model = UnivInfo
        fields = [
            'univ_name', 'email', 'tel', 'address', 'profile_pic',
        ]


class EditForm(forms.ModelForm):
    class Meta:
        model = UnivInfo
        fields = [
            'email', 'tel', 'address', 'profile_pic',
        ]


class EventForm(forms.ModelForm):
    class Meta:
        model = EventInfo
        fields = [
            'title', 'desc', 'time', 'img',
        ]