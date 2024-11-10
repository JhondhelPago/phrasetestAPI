from django.urls import path
from . import views


#urls path to fire the function associated 


urlpatterns = [

    path('test/run/api', views.teacher_api_test_run),
    path('info', views.teacherInfo),
    path('section', views.section_list_view),
    path('create/essay/assignment', views.teacher_CreateEssayAssignment),
    path('assignment/info/details', views.essay_assignment_details),
    path('section/info', views.section_details),
    path('section/new/', views.add_new_section)


]   