from django.urls import path

from .edu_views.assign import create_assign,create_detail_normative
from .edu_views.narmative import create_normative,get_normative

urlpatterns=[
    path("",create_normative,name="normative-create"),
    path("user-assign/<int:nor_pk>/",create_assign,name="user-create"),
    path("normative/list/",get_normative,name="normative-list"),
    path("normative/detail/<int:pk>/",create_detail_normative,name="detail-normative"),



]
