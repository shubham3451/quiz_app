from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.start_quiz, name='start_quiz'),
    path('question/', views.question, name='question'),
    path('results/', views.results, name='results'),
]

