from django.db import models

from account.models import CustomUser


class TeacherProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=150, blank=True, null=True)
    experience_years = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.get_full_name() or self.user.username