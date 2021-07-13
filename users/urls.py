from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('profile/<str:pk>', views.userProfile, name='user-profile'),
]
