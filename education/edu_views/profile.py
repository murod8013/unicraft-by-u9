# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render,  redirect
#
# from education.forms.student import ProfileUpdateForm
#
#
# @login_required
# def profile_view(request):
#     student = request.user.student  # OneToOne: student obj
#
#     if request.method == 'POST':
#         form = ProfileUpdateForm(request.POST, request.FILES, instance=student)
#         if form.is_valid():
#             student = form.save(commit=False)
#
#             # user fieldlarini alohida saqlash
#             user = student.user
#             full_name = request.POST.get('full_name', '').split()
#             user.first_name = full_name[0] if len(full_name) > 0 else ''
#             user.last_name = full_name[1] if len(full_name) > 1 else ''
#             user.email = request.POST.get('email', user.email)
#             user.username = request.POST.get('username', user.username)
#             user.save()
#
#             student.save()
#             return redirect('profile_view')
#         print(request.user.full_name)
#
#     else:
#         form = ProfileUpdateForm(instance=student)
#
#     return render(request, 'profile/profile.html', {'student': student, 'form': form})
#




from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from education.edu_models.profile.student import StudentProfile
from education.edu_models.student import Student
from education.forms.profile import StudentProfileForm
from education.forms.student import StudentForm

@login_required
def profile_view(request):
    user = request.user

    # Avval Student va StudentProfile obyektlarini olish yoki yaratish
    student, _ = Student.objects.get_or_create(user=user)
    student_profile, _ = StudentProfile.objects.get_or_create(user=user)
    print(student_profile.full_name, repr(student_profile.full_name))

    if request.method == 'POST':
        student_form = StudentForm(request.POST, request.FILES, instance=student)
        profile_form = StudentProfileForm(request.POST, request.FILES, instance=student_profile)


        if student_form.is_valid() and profile_form.is_valid():
            # Studentni saqlash
            student_form.save()

            # StudentProfile ni saqlash (user field albatta mavjud)
            profile_instance = profile_form.save(commit=False)
            profile_instance.user = user
            profile_instance.save()

            return redirect('profile_view')  # 'profile' URL nomi bo'lishi kerak
    else:
        student_form = StudentForm(instance=student)
        profile_form = StudentProfileForm(instance=student_profile)

    context = {
        'student_form': student_form,
        'profile_form': profile_form,
        'student': student,
        'student_profile': student_profile,

    }
    return render(request, 'profile/profile.html', context)

