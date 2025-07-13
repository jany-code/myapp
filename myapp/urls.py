from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('hello/<str:name>', views.hello),
    path('projects/', views.projects, name='projects'),
    path('details/<int:id>', views.project_detail, name='project_detail'),
    path('tasks/', views.tasks, name='tasks'),
    path('create-task/', views.create_task, name='create_task'),
    path('create-project/', views.create_project, name='create_project'),
]