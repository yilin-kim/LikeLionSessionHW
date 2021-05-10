from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    duedate = models.DateTimeField()

    def __str__(self):
        return self.title
