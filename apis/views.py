from django.shortcuts import render
from rest_framework import generics
from todolist import models
from .serializers import todoSerializer


class ListToDo(generics.ListCreateAPIView):
    queryset = models.todolist.objects.all()
    serializer_class = todoSerializer

class DetailToDo(generics.RetrieveDestroyAPIView):
    queryset = models.todolist.objects.all()
    serializer_class = todoSerializer