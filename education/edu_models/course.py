# courses/models.py
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='courses/')
    description = models.TextField(blank=True, null=True)
    duration = models.PositiveIntegerField(help_text="Davomiyligi (oylarda)")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name