
from django.shortcuts import render, get_object_or_404, redirect

from education.edu_models import Group, Student, AssignmentSubmission

from django.db.models import Count

def get_group(request):
    groups = Group.objects.annotate(students_count=Count('students'))

    context = {
        'groups': groups,
    }
    return render(request, 'group/group_list.html', context)



# def detail_group(request, pk):
#     group = Group.objects.get(pk=pk)
#     students = Student.objects.all()
#     context = {
#         'group': group ,
#         'student' : students}
#     return render(request, 'group/group_detail.html', context)

# version 1

# def detail_group(request, pk):
#     group = get_object_or_404(Group, pk=pk)
#
#     # Ushbu groupdagi studentlar
#     group_students = group.students.all()
#
#
#     # Ushbu groupga hali qo'shilmagan studentlar
#     available_students = Student.objects.exclude(id__in=group_students)
#
#     context = {
#         'group': group,
#         'group_students': group_students,
#         'available_students': available_students,
#     }
#     return render(request, 'group/group_detail.html', context)


# version 2



def detail_group(request, pk):
    group = get_object_or_404(Group, pk=pk)

    if request.method == 'POST':
        # Formdan kelgan student id lar
        student_ids = request.POST.getlist('students')
        group.students.set(student_ids)  # ManyToManyField update
        return redirect('group_detail', pk=group.pk)

    # GET request
    group_students = group.students.all()
    available_students = Student.objects.exclude(id__in=group_students)


    context = {
        'group': group,
        'group_students': group_students,
        'available_students': available_students,

    }
    return render(request, 'group/group_detail.html', context)

# def add_student_group(request, pk):
#     data=json. loads (request.body)
#     data_list=data.get("student_ids", [])
#     group = Group. objects.get(pk=pk)
#
#     with transaction. atomic():
#         student = Student. objects. filter(pk__in=data_list)
#         group. students. add( ** student)
#         group . save ()
#         return redirect("home")


# def get_detail_group_student(request, pk):
#     group = get_object_or_404(Group, pk=pk)
#     students = Student.objects.filter(groups__pk=pk)                   #temur aka version
#     print(students)
#     assign=AssignmentSubmission.objects.filter(student__in=students )
#     print(assign)
#     return render(request, 'group/group_detail_student.html', {'group': group, 'students': students, 'assign': assign})


def get_detail_group_student(request, pk):
    group = get_object_or_404(Group, pk=pk) #################
    students = Student.objects.filter(groups__pk=pk)

    # Studentlarga tegishli barcha submissions
    assign = AssignmentSubmission.objects.filter(student__in=students)                    #ai + murodjon version 🤣🤣😂😂😂

    # Faqat student ID lar ro'yxati — eng tezkor tekshirish uchun
    assign_ids = set(assign.values_list("student_id", flat=True))

    return render(request, 'group/group_detail_student.html', {
        'group': group,
        'students': students,
        'assign_ids': assign_ids
    })

