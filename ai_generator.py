import requests
import json
import openai  # only used here for the API key

def generate_blog_post(keyword, seo_data):
    prompt = f"""
    You are a professional blog writing assistant and expert content strategist.

    Write a comprehensive, long-form blog post in **Markdown format** targeting the keyword: **"{keyword}"**.

    ### 📌 Content Requirements:

    - Begin with an **engaging, SEO-optimized title** using H1 Markdown syntax (`#`).
    - Follow with a **compelling introduction** (2-3 paragraphs) that clearly introduces the topic, why it matters, and what the reader will learn.
    - Include **at least three well-structured sections** using appropriate Markdown headings (H2 and H3 as needed).
        - Each section should be informative, rich in value, and written in a friendly, expert tone.
        - Use bullet points, subheadings, or examples where helpful.
    - Include a **conclusion** that summarizes key takeaways and optionally provides a call-to-action.

    ### 🔍 SEO Stats (must be mentioned in context):
    - **Search Volume**: {seo_data['search_volume']}
    - **Keyword Difficulty**: {seo_data['keyword_difficulty']}
    - **Average CPC**: ${seo_data['avg_cpc']}

    ### 🛍 Product Recommendations:
    - Add **2-3 relevant product recommendations** in the middle or near the end.
    - For each, use a **Markdown affiliate link** with a realistic-looking URL.
    - Example: [Smart Dog Collar](https://www.superaffiliatesite.com/smart-dog-collar-aff)
    - Do **not** use placeholders like `{{AFF_LINK}}` or domains like `example.com`.

    ### 🧠 Additional Style Guidelines:
    - Write in a natural, human tone with clear, confident language.
    - Use proper Markdown formatting: headings (`#`, `##`, `###`), bold, italics, bullet points, etc.
    - Make sure the blog post is **at least 800–1200 words** in length.

    Return **only the blog post content** in Markdown format, with no extra explanation or wrapping text.
    """

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}"
    }
    payload = {
        "model": "gpt-4o-mini",
        "store": True,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code != 200:
        raise Exception(f"OpenAI API error: {response.status_code} - {response.text}")

    return response.json()["choices"][0]["message"]["content"].strip()
