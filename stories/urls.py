from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_story, name='create_story'),
    path('play_audio/<int:story_id>/', views.play_story_audio, name='play_story_audio'),
    path('<int:story_id>/update_content/', views.update_story_content, name='update_story_content'),
    path('<int:story_id>/', views.story_detail, name='story_detail'),
    # Other patterns: if you have additional ones, ensure that generic ones come last.
    path('home/', views.home, name='home'),
    path('', views.stories_list, name='stories_list'),
    path('favorites/', views.favorites_view, name='favorites'),
]
