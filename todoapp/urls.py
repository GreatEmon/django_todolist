from django.urls import path
from . import views

urlpatterns = [
    path('add_task/', views.add_task, name='add_task'),
    path('show_tasks/', views.show_tasks, name='show_tasks'),
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    path('complete_task/<int:pk>/', views.complete_task, name='complete_task'),
    path('completed_tasks/', views.completed_tasks, name='completed_tasks'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
    path('', views.home, name='home'),
]
