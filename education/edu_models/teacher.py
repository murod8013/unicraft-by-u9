# teachers/models.py
from django.db import models

from account.models import CustomUser
from education.edu_models import Course
from django.conf import settings


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to='teacher',blank=True, null=True)
    phone = models.CharField(max_length=20)
    specialization = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(help_text="Tajriba (yillarda)")
    courses = models.ManyToManyField(Course, related_name='teachers', blank=True)

    def __str__(self):
        return self.full_name