from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('upload-question/', views.upload_question, name='upload_question'),
    path('upload-answer/', views.upload_answer, name='upload_answer'),
    path('view-answers/', views.view_answers, name='view_answers'),
    path('dashboard/', views.dashboard, name='dashboard'),

]
