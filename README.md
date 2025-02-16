# 📖 Storybook Builder for Kids

## 🌟 Overview
Storybook Builder for Kids is an AI-powered web application that allows users to create **personalized children's storybooks** with AI-generated text and illustrations. The platform is built using **Django**, integrates **Hugging Face APIs** for AI-driven storytelling, and uses **Celery and Redis** for background task processing.

## ✨ Features
- 📝 **AI-Powered Story Generation** – Enter story themes, characters, and watch AI generate a full-fledged story.
- 🎨 **AI-Generated Illustrations** – Story images are created automatically using AI.
- 📖 **User Dashboard** – View, edit, and manage created stories.
- 📄 **Downloadable Stories** – Save stories as PDFs.
- ⚡ **Asynchronous Processing** – AI tasks run smoothly in the background using Celery and Redis.
- 🎨 **Kid-Friendly UI** – Simple, colorful, and easy to navigate.

---

## 🛠 Tech Stack
- **Backend:** Django (Python)
- **AI Services:** Hugging Face APIs (GPT-3, Stable Diffusion)
- **Task Queue:** Celery, Redis
- **Frontend:** Django Templates + Tailwind CSS
- **Database:** PostgreSQL / SQLite (for local development)
- **Deployment:** AWS / Heroku (Future Implementation)

---

## 🚀 Installation & Setup
To set up the project locally, follow these steps:

### **1. Clone the Repository**
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/storybook-builder-for-kids.git
cd storybook-builder-for-kids
```

### **2. Create a Virtual Environment (Recommended)**
Before installing dependencies, it's recommended to create a virtual environment to keep dependencies isolated.

Run the following command:

#### **For macOS / Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### **3. Install Dependencies**
Now, install all required dependencies using:
```bash
pip install -r requirements.txt
```
### **4. Set Up Environment Variables**
Create a .env file in the root directory and add the following keys:
```bash
SECRET_KEY=your_django_secret_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
```
 Replace "your_django_secret_key" and "your_huggingface_api_key" with actual values.

### **5. Apply Migrations & Start the Server**
Run the following commands to apply migrations and start the development server:
```bash
python manage.py migrate
python manage.py runserver
```

Now, open your browser and go to http://127.0.0.1:8000/ to see the project running. 🎉


### **📌 What’s Next?**
✅ **Copy & Paste** this into your `README.md`.  
✅ **Commit & Push** the updated README to GitHub:
```bash
git add README.md
git commit -m "Updated README with installation instructions"
git push origin main
```

### **🤝 Contributing**
**Contributions are welcome! Follow these steps:**

1. Fork the repository.
2. Create a new branch (feature-branch).
3. Make your changes and commit them.
4. Push your branch and create a Pull Request.

### **🛡 License** ###
This project is licensed under the MIT License.
