from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Todo


class TodoAPITestCase(APITestCase):
    def setUp(self):
        # Set up mock data
        Todo.objects.create(title="Buy groceries", completed=False)
        Todo.objects.create(title="Walk the dog", completed=True)

    def test_get_todo_list(self):
        response = self.client.get("/api/tasks/")
        # Verify status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify response structure
        response_data = response.json()
        self.assertIn("status", response_data)
        self.assertIn("message", response_data)
        self.assertIn("data", response_data)

    def test_get_task_detail(self):
        # Test the GET method for retrieving a todo item by ID
        response = self.client.get("/api/tasks/1/")
        self.assertEqual(response.status_code, 200)

    def test_get_task_not_found(self):
        # Test the GET method for retrieving a todo item by ID
        response = self.client.get("/api/tasks/100/")
        self.assertEqual(response.status_code, 404)

    def test_create_task(self):
        # Test the POST method for creating a new todo item
        response = self.client.post("/api/tasks/", {"title": "New Todo"})
        self.assertEqual(response.status_code, 201)

    def test_create_task_bad_request(self):
        # Test the POST method for creating a new todo item
        response = self.client.post("/api/tasks/", {})
        self.assertEqual(response.status_code, 400)

    def test_update_task(self):
        # Test the PUT method for updating an existing todo item
        response = self.client.put(
            "/api/tasks/1/", {"title": "Updated task", "completed": True}
        )
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed

    def test_update_task_not_found(self):
        # Test the PUT method for updating a todo item that doesn't exist
        response = self.client.put(
            "/api/tasks/100/", {"title": "Updated task", "completed": True}
        )
        self.assertEqual(response.status_code, 404)

    def test_update_task_bad_request(self):
        # Test the PUT method for updating a todo item
        response = self.client.put("/api/tasks/1/", {})
        self.assertEqual(response.status_code, 400)

    def test_delete_todo(self):
        # Test the DELETE method for deleting a todo item
        response = self.client.delete("/api/tasks/1/")
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed
