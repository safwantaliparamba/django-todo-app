from uuid import uuid4

from django.db import models



class Todo(models.Model):
    task = models.CharField(max_length=255)
    id = models.UUIDField(primary_key=True,unique=True,editable=False,default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task


class CompletedTodo(models.Model):
    task = models.CharField(max_length=255)
    id = models.UUIDField(primary_key=True,unique=True,editable=False,default=uuid4)
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task