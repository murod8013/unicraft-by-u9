from django.db import models

from .narmativ import Normative
from .student  import Student



class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Normative, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    file = models.FileField(upload_to='submissions/', blank=True, null=True)
    grade = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    graded_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.assignment.title} - {self.student.user.username}"