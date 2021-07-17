from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('edit-account/', views.editAccount, name='edit-account'),

    path('', views.profile, name='profile'),
    path('profile/<str:pk>', views.userProfile, name='user-profile'),
    path('account', views.userAccount, name='account'),
    path('create-skill', views.createSkill, name='create-skill'),
    path('update-skill/<str:pk>', views.updateSkill, name='update-skill'),
    path('delete-skill/<str:pk>', views.deleteSkill, name='delete-skill'),

    path('inbox/', views.inbox, name='inbox'),
    path('message/<str:pk>/', views.viewmessage, name='message'),
]
