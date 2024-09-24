from django.urls import path
from . import views


#urls paths to fire the function associated

urlpatterns = [
    path('devs/', views.devs),
    path('sample_para/', views.sample_para),
    path('submit_essay_instance/', views.submitEssayInstance),
    

]