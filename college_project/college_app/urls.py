from . import views
from django.urls import path

app_name='college_app'

urlpatterns = [
    path('',views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('fillform/', views.fillform, name='fillform'),
    path('form/', views.form, name='form'),
    path('msg/', views.msg, name='msg'),
    path('logout/', views.logout, name='logout')
]
