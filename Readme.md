# 🧠 AI-Powered SEO Blog Generator

This project is a Flask-based web application that generates long-form, SEO-optimized blog posts using OpenAI's GPT models. It integrates SEO keyword research and automatically generates and saves high-quality Markdown blog posts.

---

## 🚀 Features

- 🔍 **SEO Research**: Automatically fetches keyword stats like search volume, difficulty, and CPC.
- ✍️ **AI Content Generation**: Uses OpenAI’s GPT models (like `gpt-4o-mini`) to write blog posts.
- 🗂️ **Markdown Output**: Blog posts are saved as `.md` files with proper formatting.
- 🔄 **Background Scheduler**: Supports daily automated blog post generation via `APScheduler`.
- 🌐 **REST API**: Simple `/generate` endpoint to trigger post creation via API call.

---

## 📁 Project Structure

```text
project/
├── ai_generator.py         # Generates blog content using OpenAI
├── seo_fetcher.py          # Fetches SEO data for a keyword
├── app.py                  # Main Flask app with endpoints
├── posts/                  # Folder where generated blog posts are saved
├── .env                    # Environment variables (e.g., OpenAI key)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---
## Technologies Used

- Python
- Flask
- OpenAI API

---
## ⚙️ Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-blog-generator.git
cd ai-blog-generator
```
### 2. Create .env file
```bash
Add the Open AI API key in format below 

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
### 3.Start the Server
```bash
python app.py
```
---
## API Endpoints
GET /generate
Trigger a blog post generation by passing a keyword query parameter.
```bash
Example Request:
http://localhost:5000/generate?keyword=mobiles
```
```bash
Example Response:
{
    "file": "blogs\\mobiles.md",
    "keyword": "mobiles",
    "message": "Blog post generated and saved successfully.",
    "seo_data": {
        "avg_cpc": 1.32,
        "keyword_difficulty": 36,
        "search_volume": 27316
    }
}
```
---
## Dependencies Used

- python-dotenv
- requests
- openai
- APScheduler

---
## 📝 License
This project is licensed under the MIT License.
