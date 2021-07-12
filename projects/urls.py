from django.urls import path

from .views import *


urlpatterns = [
    path('', Index, name='index'),
    path('project/<str:pk>/', project, name='project'),
    path('create-project/', Createproject, name='create-project'),
    path('update-project/<str:pk>', Updateproject, name='update-project'),
    path('delete-project/<str:pk>', deleteProject, name='delete-project'),
]
