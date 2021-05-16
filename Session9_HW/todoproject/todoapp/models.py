from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    duedate = models.DateTimeField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasks', null=True, default=None)

    def __str__(self):
        return self.title


class Comment(models.Model):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments', null=True, default=None)
