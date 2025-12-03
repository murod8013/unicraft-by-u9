from django import forms

from education.edu_models import AssignmentSubmission


class AssignMentForm(forms.ModelForm):
    class Meta:
        model=AssignmentSubmission
        fields=[
            'text',
            'file',

        ]