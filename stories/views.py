from django.shortcuts import render, redirect, get_object_or_404
from .forms import StoryCreationForm
from .models import Story
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from gtts import gTTS
import io
from .models import Story  # Ensure you import your Story model


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

def play_story_audio(request, story_id):
    # Retrieve the story or return a 404 error if not found
    story = get_object_or_404(Story, id=story_id)
    
    # Check if the story has content to convert
    if not story.content:
        return HttpResponse("No content available for TTS", status=400)
    
    # Generate audio using gTTS (language set to English)
    tts = gTTS(text=story.content, lang='en')
    
    # Create an in-memory bytes buffer to store the audio file
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    
    # Ensure the buffer’s pointer is at the beginning
    audio_buffer.seek(0)
    
    # Return the audio data with the correct MIME type for MP3
    return HttpResponse(audio_buffer, content_type='audio/mpeg')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Story
from .forms import StoryContentUpdateForm

def update_story_content(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    if request.method == 'POST':
        form = StoryContentUpdateForm(request.POST, instance=story)
        if form.is_valid():
            form.save()
            return redirect('story_detail', story_id=story.id)
    else:
        form = StoryContentUpdateForm(instance=story)
    return render(request, 'stories/update_story_content.html', {'form': form, 'story': story})
