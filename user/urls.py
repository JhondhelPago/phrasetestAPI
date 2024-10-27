from django.urls import path
from  .import views



#urls paths to fire the function associated

urlpatterns = [
    path('devs/', views.devs),
    path('submit_essay_instance/', views.submitEssayInstance),
    path('essay/check/', views.sampleProcess),
    path('auth/login', views.login),
    path('auth/student/signup', views.signup_student),
    path('auth/teacher/signup', views.signup_teacher),
    path('auth/test', views.token_test),
    path('auth/token/test', views.new_accesstoken),
    path('auth/token/new/access', views.CustomTokenRefreshView.as_view()),
    path('auth/token/new/pair', views.CustomeTokenObtainView.as_view()),
    path('auth/otp/verify', views.otp_verify),
    path('auth/otp/reverify', views.otp_reverify),
    path('student/info', views.studentUserInfo),

    path('student', views.sample_view_get)

]