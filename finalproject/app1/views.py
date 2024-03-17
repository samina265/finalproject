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
from datetime import datetime
# Configure API key
os.environ['GOOGLE_APL_KEY'] = "AIzaSyDknfkoy5el036HU7PYy_Esd-VgBXYDVNs"
genai.configure(api_key=os.getenv("GOOGLE_APL_KEY"))

# Initialize Gemini LLM model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def main(request):
    return render(request, 'main.html')

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response


# @login_required(login_url='login_or_signup')
from datetime import datetime
import os

def home(request):
    chat_history = request.session.get('chat_history', [])
    for i, item in enumerate(chat_history):
        if len(item) < 3:
            chat_history[i] = (*item, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    res_history = []
    error_message = ''
    try:
        if request.method == 'POST':
            input_text = request.POST.get('input')
            if input_text:
                response = get_gemini_response(input_text)
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                chat_history.append(("You", input_text, current_time))
                res_history.append(("You", input_text))
                for chunk in response:
                    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    chat_history.append(("Bot", chunk.text, current_time))
                    res_history.append(("Bot", chunk.text))
                # Write chat history to a text file
                with open('chat_history.txt', 'a') as f:  # change 'w' to 'a'
                    for sender, message, time in chat_history:
                        f.write(f"{time} - {sender}: {message}\n")
                # Save chat history to session
                request.session['chat_history'] = chat_history
                 
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
            login(request, user) 
            return redirect('main')  
        elif action == 'login':
            # Handle login logic
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main') 
            else:
               return HttpResponse("Username & Password is incorrect!!!")


    return render(request, 'index.html')


    
    