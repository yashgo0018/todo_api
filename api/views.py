from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo

class TodoCreateList(APIView):
    def get(self, request, *args, **kwargs):
        return Response(TodoSerializer(Todo.objects.all(), many=True).data)

    def post(self, request, *args, **kwargs):
        title = request.data.get("title")
        notes = request.data.get("notes")
        todo = Todo(title=title, notes=notes)
        todo.save()
        return Response(TodoSerializer(todo).data)

class TodoDetail(APIView):
    def get(self, request, id, *args, **kwargs):
        todo = get_object_or_404(Todo, id=id)
        return Response(TodoSerializer(todo).data)
