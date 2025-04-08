from django.test import TestCase

# Create your tests here.
class TodoViewTestCase(TestCase):

    def test_get_todo_list(self):
        # Test the GET method for listing all todo items
        response = self.client.get("/api/todos/")
        self.assertEqual(response.status_code, 200)

    def test_get_todo_detail(self):
        # Test the GET method for retrieving a todo item by ID
        response = self.client.get("/api/todos/1/")
        self.assertEqual(response.status_code, 200)

    '''

    def test_create_todo(self):
        # Test the POST method for creating a new todo item
        response = self.client.post("/api/todos/", {"title": "New Todo"})
        self.assertEqual(response.status_code, 201)
        # Add more assertions as needed

    def test_update_todo(self):
        # Test the PUT method for updating an existing todo item
        response = self.client.put("/api/todos/1/", {"title": "Updated Todo"})
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed

    def test_delete_todo(self):
        # Test the DELETE method for deleting a todo item
        response = self.client.delete("/api/todos/1/")
        self.assertEqual(response.status_code, 204)
        # Add more assertions as needed
    '''