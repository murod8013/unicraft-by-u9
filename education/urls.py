from django.urls import path

from .edu_views.assign import create_assign, create_detail_normative, checking_assign_list, mark_assign_student
from .edu_views.group import get_group, detail_group, get_detail_group_student
from .edu_views.narmative import create_normative,get_normative
from .edu_views.profile import profile_view
from .edu_views.student import get_student

urlpatterns=[

    #normative
    path("",create_normative,name="normative-create"),
    path("normative/list/",get_normative,name="normative-list"),
    path("normative/detail/<int:pk>/",create_detail_normative,name="detail-normative"),

    #assign
    path("user-assign/<int:nor_pk>/", create_assign, name="user-create"),
    path("assign/list/",checking_assign_list,name="assign-list"),
    path("assign/detail/<int:assign_pk>/",mark_assign_student,name="assign-detail"),

    #students
    path("student/", get_student, name="student-list"),

    #group
    path("group/",get_group,name="group-list"),
    path("group/detail/<int:pk>/",detail_group,name="group_detail"),
    path("group/detail-st/<int:pk>/", get_detail_group_student, name="get_detail_group_student"),


    #profie
    path('profile/profile/', profile_view, name="profile_view"),
    ]
