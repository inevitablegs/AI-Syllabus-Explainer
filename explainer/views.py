from django.shortcuts import render

# Create your views here.
import os
import google.generativeai as genai
from django.shortcuts import render

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def home(request):
    result = None
    if request.method == "POST":
        syllabus_text = request.POST.get("syllabus")

        prompt = f"""
        I'm a student. Please analyze the following syllabus and explain each unit in simple terms. 
        Also provide 2-3 important key concepts per unit and suggest related YouTube or web resources.

        Syllabus:
        {syllabus_text}
        """

        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)
        result = format_text(response.text)

    return render(request, "explainer/home.html", {"result": result})


import re
import markdown
from html import unescape

def format_text(text: str) -> str:
    """
    Converts Gemini-style AI syllabus markdown-ish text to clean HTML using markdown module.
    """
    # Unescape HTML entities
    # text = unescape(raw_text)

    # # Remove excessive bold markers (**, ***, etc.)
    # text = re.sub(r"\*{2,}", "", text)

    # # Format Unit Headings
    # text = re.sub(r"📘\s*(Unit\s*\d+:.*?)\n?-*", r"\n## 📘 \1\n", text, flags=re.IGNORECASE)

    # # Convert labels into markdown subheadings
    # text = re.sub(r"In Simple Terms:", r"### 🧠 Simple Explanation", text)
    # text = re.sub(r"Key Concepts:", r"### 📌 Key Concepts", text)
    # text = re.sub(r"Resources:", r"### 🔗 Resources", text)
    # text = re.sub(r"YouTube:", r"#### 🎥 YouTube", text)
    # text = re.sub(r"Web:", r"#### 🌐 Web", text)

    # # Replace Gemini bullets
    # text = re.sub(r"^\s*→\s*", "* ", text, flags=re.MULTILINE)
    # text = re.sub(r"^\s*•\s*", "* ", text, flags=re.MULTILINE)

    # # Cleanup extra spacing
    # text = re.sub(r"\n{3,}", "\n\n", text).strip()

    # Convert to HTML using markdown module
    html = markdown.markdown(text, extensions=['fenced_code', 'tables'])
    return html
