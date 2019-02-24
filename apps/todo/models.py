from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField()
    finished = models.BooleanField(default=False)
