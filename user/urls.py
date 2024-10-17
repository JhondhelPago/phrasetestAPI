from django.urls import path
from . import views



#urls paths to fire the function associated

urlpatterns = [
    path('devs/', views.devs),
    path('submit_essay_instance/', views.submitEssayInstance),
    path('essay/check/', views.sampleProcess),
    path('auth/login', views.login),
    path('auth/student/signup', views.signup),
    path('auth/test', views.token_test),
    path('auth/token/test', views.new_accesstoken),
    path('auth/token/new/access', views.CustomTokenRefreshView.as_view())

]