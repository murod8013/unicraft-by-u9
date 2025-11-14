# normatives/models.py
from django.db import models
from .course import Course
from .teacher import Teacher


class Normative(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='normatives')
    mark = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='lessons/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    teacher = models.ManyToManyField(Teacher, related_name='normatives', blank=True)

    def __str__(self):
        return f"{self.title} - {self.get_lesson_type_display()}"
