from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models import CustomUser
from education.edu_models.academic.student_academic import StudentAcademic
from education.edu_models.profile.manager import ManagerProfile
from education.edu_models.profile.parent import ParentProfile
from education.edu_models.profile.student import StudentProfile
from education.edu_models.profile.teacher import TeacherProfile


@receiver(post_save, sender=CustomUser)
def create_user_profiles(sender, instance, created, **kwargs):
    if created:
        # STUDENT
        if instance.role == 'student':
            StudentProfile.objects.create(user=instance)
            StudentAcademic.objects.create(user=instance)

        # TEACHER
        elif instance.role == 'teacher':
            TeacherProfile.objects.create(user=instance)

        # PARENT
        elif instance.role == 'parent':
            ParentProfile.objects.create(user=instance)

        # MANAGER
        elif instance.role == 'manager':
            ManagerProfile.objects.create(user=instance)
