from django.urls import path 
from .views import *

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()), #after URL Enter /id of task specific task will be open
    path('', ListTodo.as_view()),            #View all list on URL
    path('create', CreateTodo.as_view()),    #Create task by entering /create after URl
    path('update/<int:pk>', UpdateTodo.as_view()), #Update task 
    path('delete/<int:pk>', DeleteTodo.as_view())   # Delete task
]