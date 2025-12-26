from django.db import models

from account.models import CustomUser


class StudentAcademic(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    courses = models.ManyToManyField('course', related_name='students', blank=True)

    def __str__(self):
        return f"{self.user.username} - Academic Data"
