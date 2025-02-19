from celery import shared_task
from .models import Story
from .utils import generate_story_text, generate_story_image

@shared_task
def generate_story_and_image_task(story_id):
    try:
        story = Story.objects.get(id=story_id)
    except Story.DoesNotExist:
        return "Story not found."

    # Generate story text and illustration
    generated_text = generate_story_text(
        f"Write a creative story about {story.title} with characters {story.characters} in a {story.theme} setting."
    )
    generated_image_url = generate_story_image(f"Generate an illustration for a story titled {story.title}")

    # Update the story record with the AI-generated content
    story.content = generated_text
    story.illustration_url = generated_image_url  # Assuming your Story model has this field
    story.status = 'completed'
    story.save()
    return "Story generation completed."
