from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.HomeView.as_view(), name='home'),
    path('add/', views.add_task, name='add'),
    path('completed/<todo_id>/', views.completed_task, name='completed'),
    path('uncompleted/<todo_id>/', views.uncompleted_task, name='uncompleted'),
    path('delete/<todo_id>/', views.delete_one, name='delete_one'),
    path('del_completed/', views.delete_completed, name='delete_completed'),
    path('del_all/', views.delete_all, name='delete_all'),
    path('edit/<todo_id>/', views.edit, name='edit'),
    path('save/<todo_id>/', views.save, name='save'),
]


