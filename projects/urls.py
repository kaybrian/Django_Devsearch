from django.urls import path

from .views import *


urlpatterns = [
    path('', Index, name='index'),
    path('project/<str:pk>/', project, name='project'),
    path('create-project/', Createproject, name='create-project'),
]
