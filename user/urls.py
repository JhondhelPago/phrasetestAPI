from django.urls import path
from . import views



#urls paths to fire the function associated

urlpatterns = [
    path('devs/', views.devs),
    path('submit_essay_instance/', views.submitEssayInstance),
    path('essay/check/', views.sampleProcess)

]