# stories/tasks.py
from celery import shared_task
from .models import Story
from .utils import generate_story_text, generate_story_image

@shared_task
def generate_story_and_image_task(story_id):
    """
    Celery task to generate story content and illustration using Hugging Face APIs.
    Updates the Story record with the generated text and image URL.
    """
    try:
        story = Story.objects.get(id=story_id)
    except Story.DoesNotExist:
        return "Story not found."
    
    # Build prompt for text generation
    text_prompt = (
        f"Write a creative and engaging story titled '{story.title}' that involves characters: {story.characters}. "
        f"The story should be set in {story.setting} and explore the theme of {story.theme}."
    )
    generated_text = generate_story_text(text_prompt)
    
    # Build prompt for image generation (you can fine-tune this as needed)
    image_prompt = f"A colorful illustration for a children's story titled '{story.title}' set in {story.setting}."
    generated_image_url = generate_story_image(image_prompt, use_alternative=True)  # Using Stable Diffusion XL for better quality
    
    # Update the Story record
    story.content = generated_text
    story.illustration_url = generated_image_url
    story.status = 'completed'
    story.save()
    return "AI generation completed."
