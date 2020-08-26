from django.db import models
from django.utils import timezone


class Todo(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    task = models.CharField(max_length=100)
    story = models.CharField(max_length=100, default="-")
    project = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task


class TodoArchive(Todo):
    date_archived = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'ARCH {self.task} - {self.date_added}'
