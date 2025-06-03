from flask import Flask, request, jsonify
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
import os
from ai_generator import generate_blog_post
from seo_fetcher import fetch_seo_data
from datetime import datetime

load_dotenv()
app = Flask(__name__)
scheduler = BackgroundScheduler()
scheduler.start()

def save_post(keyword, content):
    filename = f"example_{keyword.replace(' ', '_')}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

@app.route("/generate")
def generate():
    keyword = request.args.get("keyword")
    if not keyword:
        return jsonify({"error": "Keyword parameter is required"}), 400

    seo_data = fetch_seo_data(keyword)
    content = generate_blog_post(keyword, seo_data)

    # Create markdown content with metadata
    markdown_content = f"""# Blog Post: {keyword}

**SEO Stats**  
- Search Volume: {seo_data['search_volume']}  
- Keyword Difficulty: {seo_data['keyword_difficulty']}  
- Avg CPC: ${seo_data['avg_cpc']}

---

{content}
"""

    os.makedirs("blogs", exist_ok=True)

    # Save to markdown file
    file_path = os.path.join("blogs", f"{keyword.replace(' ', '_').lower()}.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    return jsonify({
        "keyword": keyword,
        "seo_data": seo_data,
        "file": file_path,
        "message": "Blog post generated and saved successfully."
    }), 200


def daily_job():
    keyword = "wireless earbuds"
    seo_data = fetch_seo_data(keyword)
    content = generate_blog_post(keyword, seo_data)
    save_post(keyword, content)
    print(f"[{datetime.now()}] Generated blog post for '{keyword}'")

# Daily at 10:00 AM
scheduler.add_job(daily_job, 'cron', hour=10, minute=0)

if __name__ == "__main__":
    app.run(debug=True)
