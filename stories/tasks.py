# stories/tasks.py
from celery import shared_task
import requests  # For example purposes if you're calling an external API

@shared_task
def generate_story_task(prompt):
    """
    Task to generate a story using an external AI service.
    Replace this with your actual API call to Hugging Face or any other service.
    """
    # Example: simulate an API call
    # response = requests.post("https://api.huggingface.co/...", json={"prompt": prompt})
    # story_text = response.json().get("story", "No story generated.")
    # For now, we simulate with a placeholder:
    story_text = f"Generated story based on prompt: {prompt}"
    return story_text
