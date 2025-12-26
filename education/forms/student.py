# forms.py
from django import forms
from education.edu_models.student import Student

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['phone', 'avatar']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['avatar', 'phone', 'email', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}) , # ✅ bitta date picker input
        }