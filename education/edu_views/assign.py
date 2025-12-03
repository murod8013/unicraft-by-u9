from django.shortcuts import redirect, render
from education.edu_models import Normative

from education.forms.assigntment import AssignMentForm

from education.edu_models import Student


def create_assign(request,nor_pk):
    pk=Normative.objects.get(pk=nor_pk)
    user=request.user
    student=Student.objects.get(user=user)
    if request.method=='POST':
        form=AssignMentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.student=student
            form.normative=pk
            form.save(commit=True)
            return redirect("home")
    else:
        form=AssignMentForm()
    return render(request,"normative/create_assign.html",{'form':form})



def create_detail_normative(request,pk):
    user=request.user
    student=Student.objects.get(user=user.pk)
    normative=Normative.objects.get(pk=pk)
    if request.method=='POST':
        form=AssignMentForm(request.POST,request.FILES)
        if form.is_valid():
            assign=form.save(commit=False)
            assign.student=student
            assign.assignment=normative
            assign.save()
            return redirect("home")
    else:
        form=AssignMentForm()
    context={
        'form':form,
        'normative':normative
    }
    return render(request,"assign/create.html",context)