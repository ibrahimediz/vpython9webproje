from django.shortcuts import render
# from rest_framework import generics
from rest_framework import viewsets
from todolist import models
from .serializers import todoSerializer


# class ListToDo(generics.ListCreateAPIView):
#     queryset = models.todolist.objects.all()
#     serializer_class = todoSerializer

# class DetailToDo(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.todolist.objects.all()
#     serializer_class = todoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.todolist.objects.all()
    serializer_class = todoSerializer    