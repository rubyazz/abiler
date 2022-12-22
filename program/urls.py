
from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    # path('program/', views.index, name='index'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('abiler/', views.abi, name='abi'),
    path('help/', views.help, name='help'),
    #path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('event/new/', views.event, name='event_new'),
    path('event/edit/<event_id>/', views.event, name='event_edit'),
]