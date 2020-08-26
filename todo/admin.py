from django.contrib import admin
from .models import Todo, TodoArchive

admin.site.register(Todo)
admin.site.register(TodoArchive)
