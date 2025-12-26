from django.db import models

from account.models import CustomUser


class ParentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    child_name = models.CharField(max_length=150)
    child_group = models.CharField(max_length=150)

    def __str__(self):
        return f"Parent: {self.user.username}"