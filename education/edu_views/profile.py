from django.contrib.auth.decorators import login_required
from django.shortcuts import render,  redirect

from education.forms.student import ProfileUpdateForm


@login_required
def profile_view(request):
    student = request.user.student  # OneToOne: student obj

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            student = form.save(commit=False)

            # user fieldlarini alohida saqlash
            user = student.user
            full_name = request.POST.get('full_name', '').split()
            user.first_name = full_name[0] if len(full_name) > 0 else ''
            user.last_name = full_name[1] if len(full_name) > 1 else ''
            user.email = request.POST.get('email', user.email)
            user.username = request.POST.get('username', user.username)
            user.save()

            student.save()
            return redirect('profile_view')
        print(request.user.full_name)

    else:
        form = ProfileUpdateForm(instance=student)

    return render(request, 'profile/profile.html', {'student': student, 'form': form})




