from django.db import models

from account.models import CustomUser


class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=150)
    birth_date = models.DateField(blank=True, null=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
