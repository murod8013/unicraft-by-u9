from django import forms
from education.edu_models.student import Student
from education.edu_models.profile.student import StudentProfile


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['full_name', ]
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'style': 'display:none;'}),

        }