# groups/models.py
from django.db import models


from .course import Course
from .teacher import Teacher
from .student import Student


class Group(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='groups')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='groups')
    students = models.ManyToManyField(Student, related_name='groups', blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.course.name})"