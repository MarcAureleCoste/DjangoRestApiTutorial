from rest_framework import viewsets

from .models import (
    Todo,
    TodoUser
)
from .serializers import TodoSerializer
from .filters import TodoFilter


# Create your views here.
class TodoViewset(viewsets.ModelViewSet):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_class = TodoFilter

    def filter_queryset(self, queryset):
        todo_user = TodoUser.objects.get(d_user=self.request.user)
        return queryset.filter(owner=todo_user)
