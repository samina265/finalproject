from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from PIL import Image
import os
import google.generativeai as genai

def load_dotenv():
    # Load environment variables here
    pass

load_dotenv()
os.environ['GOOGLE_APL_KEY'] = "AIzaSyDknfkoy5el036HU7PYy_Esd-VgBXYDVNs"
genai.configure(api_key=os.getenv("GOOGLE_APL_KEY"))

model = genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(image):
    if image is None:
        return None
    response = model.generate_content(image)
    return response.text if response else None

def upload_image(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        image = Image.open(fs.path(name))
        context['uploaded_file'] = fs.url(name)
        context['filename'] = uploaded_file.name  # pass the filename to the template
        response = get_gemini_response(image)
        context['response'] = response
    return render(request, 'upload.html', context)