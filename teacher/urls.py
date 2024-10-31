from django.urls import path
from . import views


#urls path to fire the function associated 


urlpatterns = [

    path('test/run/api', views.teacher_api_test_run),
    path('info', views.teacherInfo)


]   