import requests

def generate_story_text(prompt):
    # Dummy endpoint; replace with your actual AI API call (e.g., Hugging Face)
    api_url = "https://api.example.com/generate_text"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    payload = {"prompt": prompt, "max_length": 500}
    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data.get('generated_text', '')
    return "Error generating story text."

def generate_story_image(prompt):
    # Dummy endpoint; replace with your actual image generation API call (e.g., Stable Diffusion)
    api_url = "https://api.example.com/generate_image"
    headers = {"Authorization": "Bearer YOUR_IMAGE_API_KEY"}
    payload = {"prompt": prompt, "num_images": 1}
    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data.get('image_url', '')
    return ""
