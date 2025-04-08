from django.urls import path

from todolistapp.views import TodoView, TodoViewDetails

urlpatterns = [
    path("tasks/", TodoView.as_view()),
    path("tasks/<int:id>/", TodoViewDetails.as_view()),
]
