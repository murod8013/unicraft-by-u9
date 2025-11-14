# students/models.py
from django.db import models

from account.models import CustomUser
from education.edu_models import Course
from django.conf import settings


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='student',blank=True, null=True)
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    birth_date = models.DateField()
    registered_at = models.DateTimeField(auto_now_add=True)
    # courses = models.ManyToManyField(Course, related_name='students', blank=True)

    def __str__(self):
        return self.full_name