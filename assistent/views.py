from urllib import response
from django.shortcuts import render
from .forms import BlogForm
from django.http import HttpResponse
# from ollama import chat  # ✅ Ensure `ollama` is properly installed and configured

def assistent(request):
    """
    Handles GET and POST requests for the AI assistant form.
    - GET: renders an empty form
    - POST: processes the form, sends prompt to Ollama, and returns the AI response
    """
    result = ""

    if request.method == "POST":
        form = BlogForm(request.POST)

        if form.is_valid():
            topic = form.cleaned_data.get('topic')
            text = form.cleaned_data.get('text')
            tone = form.cleaned_data.get('tone')

            # Construct appropriate prompt based on input
            if topic:
                prompt = f"Generate 2 blog ideas for the topic: '{topic}'"
            elif text and tone:
                prompt = f"Rewrite the following text in a {tone} tone:\n\n{text}"
            else:
                return HttpResponse("❗ Please provide either a topic OR both text and tone.")

            # Call Ollama API
            try:
                # response = chat(
                #     model='llama3',  # ✅ Make sure this model is available in your Ollama setup
                #     messages=[
                #         {
                #             "role": "user",
                #             "content": prompt
                #         }
                #     ]
                # )
                result = response['message']['content']  # ✅ Fixed: Access response dict properly
            except Exception as e:
                result = f"🚫 Error connecting to Ollama: {str(e)}"

            return HttpResponse(result)
    else:
        form = BlogForm()

    # Render form template
    return render(request, "assistent/index.html", {"form": form})
