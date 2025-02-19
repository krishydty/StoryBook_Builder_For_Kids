# stories/utils.py
import requests
from django.conf import settings

def generate_story_text(prompt):
    """
    Calls Hugging Face Inference API for Mistral-7B-Instruct-v0.3 to generate story text.
    """
    api_url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
    headers = {"Authorization": f"Bearer {settings.HUGGINGFACEHUB_API_TOKEN}"}
    payload = {"inputs": prompt}
    response = requests.post(api_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        output = response.json()
        try:
            # Adjust according to API response structure; here we assume first item has generated text.
            generated_text = output[0].get('generated_text', '')
        except (IndexError, AttributeError):
            generated_text = "No text generated."
        return generated_text
    else:
        return f"Error: {response.status_code} - {response.text}"

def generate_story_image(image_prompt, use_alternative=False):
    """
    Calls Hugging Face Inference API for image generation.
    By default, it uses Stable Diffusion 2. If use_alternative is True, it uses Stable Diffusion XL.
    """
    if use_alternative:
        api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl"
    else:
        api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
        
    headers = {"Authorization": f"Bearer {settings.HUGGINGFACEHUB_API_TOKEN}"}
    payload = {"inputs": image_prompt}
    response = requests.post(api_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        output = response.json()
        try:
            # Adjust based on actual response; assume first item contains the image URL.
            image_url = output[0].get('generated_image_url', '')
        except (IndexError, AttributeError):
            image_url = ""
        return image_url
    else:
        return f"Error: {response.status_code} - {response.text}"
