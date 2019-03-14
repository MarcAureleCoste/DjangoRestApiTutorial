from rest_framework.serializers import ModelSerializer
from .models import (
    Todo,
    TodoUser
)

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'id',
            'title',
            'description',
            'finished'
        )
        extra_kwargs = {
            'id': {'read_only': True}
        }

    def create(self, validated_data):
        request_user = self.context['request'].user
        todo_user = TodoUser.objects.get(d_user=request_user)
        todo = Todo.objects.create(**validated_data, owner=todo_user)
        todo.save()
        return todo
