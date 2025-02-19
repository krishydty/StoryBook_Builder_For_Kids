import requests
from django.conf import settings

def generate_story_text(prompt):
    """
    Calls the Hugging Face Inference API for the Mistral-7B-Instruct-v0.3 model
    to generate story text based on the provided prompt.

    Args:
        prompt (str): The prompt describing the story requirements.

    Returns:
        str: The generated story text, or an error message if the API call fails.
    """
    api_url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
    headers = {"Authorization": f"Bearer {settings.HUGGINGFACEHUB_API_TOKEN}"}
    payload = {"inputs": prompt}
    response = requests.post(api_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        output = response.json()
        # Expected output: a list of results; we assume the generated text is in the first item.
        try:
            # Depending on API structure, adjust the following:
            generated_text = output[0].get('generated_text', '')
        except (IndexError, AttributeError):
            generated_text = "No text generated."
        return generated_text
    else:
        return f"Error: {response.status_code} - {response.text}"

def generate_story_image(image_prompt, use_alternative=False):
    """
    Calls the Hugging Face Inference API to generate an image for the story.
    By default, it uses Stable Diffusion 2. If use_alternative is True, it uses
    Stable Diffusion XL for higher quality image generation.

    Args:
        image_prompt (str): The prompt for image generation.
        use_alternative (bool): If True, uses the alternative model (Stable Diffusion XL).

    Returns:
        str: The URL of the generated image, or an error message if the API call fails.
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
            # Adjust this based on the exact output format from the API.
            image_url = output[0].get('generated_image_url', '')
        except (IndexError, AttributeError):
            image_url = ""
        return image_url
    else:
        return f"Error: {response.status_code} - {response.text}"
