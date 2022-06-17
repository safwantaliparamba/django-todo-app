from django.contrib import admin
from .models import Todo, CompletedTodo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ['id','task','created_at']

class CompletedTodoAdmin(admin.ModelAdmin):
    list_display = ['id','task','completed_at']

admin.site.register(Todo,TodoAdmin)
admin.site.register(CompletedTodo,CompletedTodoAdmin)