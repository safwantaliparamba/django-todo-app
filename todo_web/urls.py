from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('',views.index,name='index'),
    path('todo/new/',views.addNewTodo,name='add_new'),
    path('todo/delete/<str:id>/',views.deleteTodo,name='delete_todo'),
    path('todo/completed/<str:id>/',views.completedTodo,name='completed_todo'),
    path('todo/completed/delete/<str:id>/',views.deleteCompletedTodo,name='delete_completed_todo'),
    path('todo/completed/revert/<str:id>/',views.revertCompletedTodo,name='revert_completed_todo'),
]
