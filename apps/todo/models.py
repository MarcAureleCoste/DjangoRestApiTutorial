from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    owner = models.ForeignKey('TodoUser', on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField()
    finished = models.BooleanField(default=False)


class TodoUser(models.Model):
    d_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.d_user.username
