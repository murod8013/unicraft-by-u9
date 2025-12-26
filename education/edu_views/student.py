from django.shortcuts import render

from education.edu_models import Student




def get_student(request):
    students = Student.objects.all()
    # data = student.assign_student.all()
    assigns = [st.assign_student for st in students]
    context = {
        'student': students,
        'assigns': assigns
    }
    return render(request, 'student/student_list.html' , context)

#
# def student_group_list(request):
#     student = Student.objects.all()
#     group = Group.objects.all()
#     context = {'students': student, 'groups': group}
#     return render(request, 'student/student_group_list.html' , context)








