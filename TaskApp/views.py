from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from TaskApp.models import Tasks
from TaskApp.serializers import TaskSerializer

# Create your views here.


@csrf_exempt
def taskApi(request, id=0):
    if request.method == 'GET':
        tasks = Tasks.objects.all()
        task_serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(task_serializer.data, safe=False)
    elif request.method == 'POST':
        task_data = JSONParser().parse(request)
        task_serializer = TaskSerializer(data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse(task_serializer.data, safe=False)
        else:
            return JsonResponse("Failed to add the task")
    elif request.method == 'PUT':
        task_data = JSONParser().parse(request)
        task = Tasks.objects.get(TaskId=task_data['TaskId'])
        task_serializer = TaskSerializer(task, data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse(task_serializer.data, safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        task = Tasks.objects.get(TaskId=id)
        task.delete()
        return JsonResponse("Deleted Succesfully", safe=False)
