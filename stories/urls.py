from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_story, name='create_story'),
    path('<int:story_id>/', views.story_detail, name='story_detail'),
    path('play_audio/<int:story_id>/', views.play_story_audio, name='play_story_audio'),
    path('update_content/<int:story_id>/', views.update_story_content, name='update_story_content'),


]
