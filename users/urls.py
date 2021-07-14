from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('', views.profile, name='profile'),
    path('profile/<str:pk>', views.userProfile, name='user-profile'),
]
