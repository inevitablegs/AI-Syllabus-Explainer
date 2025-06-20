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


import markdown


def format_text(text: str) -> str:
    """
    Converts Gemini-style AI syllabus markdown-ish text to clean HTML using markdown module.
    """
    import markdown
    # Convert to HTML using markdown module
    html = markdown.markdown(text, extensions=['fenced_code', 'tables'])
    return html
