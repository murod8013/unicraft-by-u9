from django.db import models

from account.models import CustomUser


class ManagerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department = models.CharField(max_length=150)

    def __str__(self):
        return f"Manager: {self.user.username}"