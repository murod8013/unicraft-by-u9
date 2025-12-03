from django import forms

from education.edu_models import Normative


class NormativeForm(forms.ModelForm):
    class Meta:
        model=Normative
        fields=[
            'course',
            'title',
            'description',
            'file',
            'teacher'
        ]