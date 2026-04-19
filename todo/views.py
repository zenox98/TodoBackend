from typing import Any

from django.db.models import QuerySet
from rest_framework import generics, permissions

from .models import Todo
from .serializers import TodoSerializer


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request: Any, _view: Any, obj: Todo) -> bool:
        return obj.user == request.user


class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self) -> QuerySet[Todo]:
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer: Any) -> None:
        serializer.save(user=self.request.user)


class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner,
    )

    def get_queryset(self) -> QuerySet[Todo]:
        return Todo.objects.filter(user=self.request.user)
