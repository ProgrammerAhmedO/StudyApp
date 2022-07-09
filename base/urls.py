from . import views
from django.urls import path


urlpatterns = [
    path('', views.home , name ='home'),
    path('room/<str:pk>', views.room , name ='room'),
    path('CreateRoom', views.CreateRoom , name ='CreateRoom'),   
    path('UpdateRoom/<str:pk>', views.UpdateRoom , name ='UpdateRoom'),   
    path('DeleteRoom/<str:pk>', views.DeleteRoom , name ='DeleteRoom'),   
    path('login/', views.loginPage , name ='login'), 
    path('logout/', views.logoutuser , name ='logout'), 
    path('profile/<str:pk>', views.profile , name ='profile'), 
    path('delete-message/<str:pk>' ,views.deleteMessage, name='delete-message'),
    path('update-message/<str:pk>' ,views.updateMessage, name='update-message'),
    path('delete-activites/<str:pk>' ,views.deleteActivites, name='delete-activites'),

]
