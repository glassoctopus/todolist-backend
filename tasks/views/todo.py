from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tasks.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed', 'temporary_field')
        depth = 2

class TodoView(ViewSet):
    def retrieve(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
            serializer = TodoSerializer(todo, context={'request': request})
            return Response(serializer.data)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        todo = Todo.objects.create(
            title=request.data['title'],
            description=request.data['description'],
            completed=request.data['completed'],
            temporary_field=request.data['temporary_field']
        )
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
            todo.title = request.data['title']
            todo.description = request.data['description']
            todo.completed = request.data['completed']
            todo.temporary_field = request.data['temporary_field']
            todo.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
