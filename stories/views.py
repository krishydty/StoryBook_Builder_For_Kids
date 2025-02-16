from django.shortcuts import render, redirect, get_object_or_404
from .forms import StoryCreationForm
from .models import Story

def create_story(request):
    if request.method == 'POST':
        form = StoryCreationForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.user = request.user  # Ensure user is assigned
            story.save()
            return redirect('story_detail', story_id=story.id)
    else:
        form = StoryCreationForm()
    return render(request, 'stories/create_story.html', {'form': form})

def story_detail(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    return render(request, 'stories/story_detail.html', {'story': story})
