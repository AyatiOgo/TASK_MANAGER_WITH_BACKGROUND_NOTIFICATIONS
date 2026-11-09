from django.shortcuts import render
from .serializer import TaskSerializer
from .models import TaskModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import send_task_notification

# Create your views here.

class TaskView(APIView):
    def get(self, request):
        task = TaskModel.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():

            task = serializer.save()
            send_task_notification.delay(task.id)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailView(APIView):
    def get(self, request, pk):
        task= TaskModel.objects.get(id=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #Updating a task
    def put(self, request, pk):
        task = TaskModel.objects.get(id=pk)
        serializer = TaskSerializer(task, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)#
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)