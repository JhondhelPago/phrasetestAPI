from django.urls import path
from . import views


#urls path to fire the function associated 


urlpatterns = [

    path('test/run/api', views.student_api_test_run),
    path('info/', views.studentInfo)

]   