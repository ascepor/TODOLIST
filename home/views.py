from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from .Serializers import * 
from .models import *
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import permissions, authentication

# basic authentication
@permission_classes([permissions.IsAuthenticated])
@authentication_classes([authentication.BasicAuthentication])

class ListTodo(generics.ListCreateAPIView):                #Read
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DetailTodo(generics.RetrieveAPIView):               #Read one task
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class UpdateTodo(generics.UpdateAPIView):              #Update
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer    

    def get_queryset(self):
        queryset = ToDo.objects.all()
        return queryset 

class CreateTodo(generics.CreateAPIView):                #Create
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def get_queryset(self):
        queryset = ToDo.objects.all()
        return queryset

class DeleteTodo(generics.DestroyAPIView):              #Deleate
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer