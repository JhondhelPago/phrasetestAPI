from django.urls import path
from . import views


#urls path to fire the function associated 


urlpatterns = [

    path('test/run/api', views.student_api_test_run),
    path('info/', views.studentInfo),
    path('assignments/', views.studentAssignments),
    # path('assignment/new/', views.studentAssignments_new),
    path('assignment/finished/', views.studentAssignmentFinished),
    path('submit/assignment/', views.studentEssaySubmit),
    path('check/assignment/submit', views.checkAssignmentDone),
    path('assignment/results/', views.getAssignmentResults),
    path('join/class/', views.JoinClass)

]   