from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todo
from .serializers import TodoSerializer
from .utils import flatten_errors


def welcome_view(request):
    return HttpResponse(
        """
        <h1>Welcome to the Todo List API!</h1>
        <p>Available endpoints:</p>
        <ul>
            <li>/admin - Admin interface</li>
            <li>/api - Your API endpoints</li>
        </ul>
    """
    )


class TodoView(APIView):
    """
    View to get all and create item task.
    """

    def get(self, request):
        """
        List all task items.
        """
        try:
            todos = Todo.objects.all()
            serializer = TodoSerializer(todos, many=True)
            return Response(
                {
                    "status": "success",
                    "message": "Todos retrieved successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"status": "error", "message": "Internal server error", "data": None},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def post(self, request, format=None):
        """
        Create a new todo item.
        """
        try:
            serializer = TodoSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(
                    {
                        "status": "error",
                        "message": "Validation failed",
                        "data": flatten_errors(serializer.errors),
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            serializer.save()
            return Response(
                {
                    "status": "success",
                    "message": "Todo created successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response(
                {"status": "error", "message": "Internal server error", "data": None},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class TodoViewDetails(APIView):
    def get(self, request, id):
        """
        List a task by id.
        """
        try:
            todo = Todo.objects.get(id=id)
            serializer = TodoSerializer(todo)
            return Response(
                {
                    "status": "success",
                    "message": "Todo retrieved successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except Todo.DoesNotExist:
            return Response(
                {"status": "error", "message": "Todo item not found", "data": None},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"status": "error", "message": "Internal server error", "data": None},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def put(self, request, id):
        """
        Update an existing todo item.
        """
        try:
            todo = Todo.objects.get(id=id)
            serializer = TodoSerializer(todo, data=request.data)

            if not serializer.is_valid():
                return Response(
                    {
                        "status": "error",
                        "message": "Validation failed",
                        "data": flatten_errors(serializer.errors),
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            serializer.save()
            return Response(
                {
                    "status": "success",
                    "message": "Todo updated successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except Todo.DoesNotExist:
            return Response(
                {"status": "error", "message": "Todo item not found", "data": None},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"status": "error", "message": "Internal server error", "data": None},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def delete(self, request, id):
        """
        Delete logical an existing todo item.
        """
        try:
            todo = Todo.objects.get(id=id)
            todo.deleted = True
            todo.save()
            return Response(
                {
                    "status": "success",
                    "message": "Todo deleted successfully",
                    "data": None,
                },
                status=status.HTTP_200_OK,
            )
        except Todo.DoesNotExist:
            return Response(
                {"status": "error", "message": "Todo item not found", "data": None},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"status": "error", "message": "Internal server error", "data": None},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
