# Схемы URL для приложения learning_logs

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [     
    path('', views.index, name='index'),   # Home page
    path('topics/', views.topics, name='topics'), # Topics page
    path('toggle_entry_completion/<int:entry_id>/', views.toggle_entry_completion, name='toggle_entry_completion'),
    path('topics/<int:topic_id>/', views.topic, name='topic'), # Info about Topic
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
