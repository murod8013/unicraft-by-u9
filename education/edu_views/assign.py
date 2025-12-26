from django.shortcuts import redirect, render
from education.edu_models import Normative, AssignmentSubmission

from education.forms.assigntment import AssignMentForm, CheckinAssignmentForm

from education.edu_models import Student


def create_assign(request, nor_pk):
    pk = Normative.objects.get(pk=nor_pk)
    user = request.user
    student = Student.objects.get(user=user)
    if request.method == 'POST':
        form = AssignMentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.student = student
            form.normative = pk
            form.save(commit=True)
            return redirect("home")
    else:
        form = AssignMentForm()
    return render(request, "normative/create_assign.html", {'form': form})


def create_detail_normative(request, pk):
    user = request.user
    student = Student.objects.get(user=user.pk)
    normative = Normative.objects.get(pk=pk)
    if request.method == 'POST':
        form = AssignMentForm(request.POST, request.FILES)
        if form.is_valid():
            assign = form.save(commit=False)
            assign.student = student
            assign.assignment = normative
            assign.save()
            return redirect("home")
    else:
        form = AssignMentForm()
    context = {
        'form': form,
        'normative': normative
    }
    return render(request, "assign/create.html", context)


def checking_assign_list(request):
    assigns = AssignmentSubmission.objects.filter(is_checked=False)
    context = {
        'assigns': assigns
    }
    return render(request, "assign/checking_list.html", context)


def mark_assign_student(request, assign_pk):
    assign = AssignmentSubmission.objects.get(pk=assign_pk)
    if request.method == 'POST':
        form = CheckinAssignmentForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            assign.mark = form.cleaned_data.get("mark")
            assign.comment = form.cleaned_data.get("comment")
            assign.is_checked = True
            assign.save()
            print(assign)
            return redirect("home")
    else:
        form = CheckinAssignmentForm()
    return render(request, "assign/mark_assign.html", {'form': form, 'assign': assign})
