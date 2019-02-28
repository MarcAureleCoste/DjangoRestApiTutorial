from rest_framework import viewsets

from .models import Todo
from .serializers import TodoSerializer
from .filters import TodoFilter


# Create your views here.
class TodoViewset(viewsets.ModelViewSet):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_class = TodoFilter
