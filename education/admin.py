from django.contrib import admin

from .edu_models import Course, Group, Normative, Student, Teacher, AssignmentSubmission

# Register your models here.
admin.site.register(Course)
admin.site.register(Group)
admin.site.register(Normative)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(AssignmentSubmission)
