# app1/views.py
from django.shortcuts import redirect, render
import os
import google.generativeai as genai
from django.http import HttpResponse
import os
from django.shortcuts import render
import google.generativeai as genai
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Configure API key
os.environ['GOOGLE_APL_KEY'] = "AIzaSyDknfkoy5el036HU7PYy_Esd-VgBXYDVNs"
GOOGLE_APL_KEY=""
genai.configure(api_key=os.getenv("GOOGLE_APL_KEY"))

# Initialize Gemini LLM model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response
chat_history = []

#@login_required(login_url='login_or_signup')
def home(request):
    res_history = []
    error_message = ''
    try:
        if request.method == 'POST':
            input_text = request.POST.get('input')
            if input_text:
                response = get_gemini_response(input_text)
                chat_history.append(("You", input_text))
                res_history.append(("You", input_text))
                for chunk in response:
                    chat_history.append(("Bot", chunk.text))
                    res_history.append(("Bot", chunk.text))
                # Write chat history to a text file
                with open('chat_history.txt', 'w') as f:
                    for sender, message in chat_history:
                        f.write(f"{sender}: {message}\n")
                 
    except Exception as e:
        error_message = str(e)
    google_api_key = os.environ.get('GOOGLE_APL_KEY')
    return render(request, 'home.html', {'chat_history': chat_history, 'res_history': res_history, 'google_api_key': google_api_key, 'error_message': error_message})


def login_or_signup(request):
    if request.method == 'POST':
        action = request.POST.get('action')  # Retrieve the action parameter from POST data
        if action == 'signup':
            # Handle signup logic
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('home') # Log in the user after signup
        elif action == 'login':
            # Handle login logic
            username = request.POST.get('username')
            pass1= request.POST.get('password')
            user = authenticate(request, username=username, password=pass1)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
               return HttpResponse("Username & Password is incorrect!!!")

    # If the request method is not POST or the action is not valid, render the index.html template
    return render(request, 'index.html')

    
    

