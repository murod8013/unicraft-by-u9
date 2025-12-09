# forms.py
from django import forms
from education.edu_models.student import Student

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['phone', 'avatar']
