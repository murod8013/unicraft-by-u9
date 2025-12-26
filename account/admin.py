from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    CustomUser )

from education.edu_models.academic.student_academic import StudentAcademic
from education.edu_models.profile.manager import ManagerProfile
from education.edu_models.profile.parent import ParentProfile
from education.edu_models.profile.student import StudentProfile
from education.edu_models.profile.teacher import TeacherProfile

admin.site.register(CustomUser)
admin.site.register(StudentProfile)
admin.site.register(StudentAcademic)
admin.site.register(TeacherProfile)
admin.site.register(ParentProfile)
admin.site.register(ManagerProfile)


# admin.py

