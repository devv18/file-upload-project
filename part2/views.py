from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate ,login



def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'username is already taken')
            return redirect('/register/')
        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        
        return redirect('/signin/')
    
    return render(request, 'register.html')
def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            mail= user.email
            return render(request,'home.html' ,{'email':mail})
        else:
            messages.info(request,'invalid username or password')
            return redirect('signin')
    return render(request,'login.html') 
from .models import UploadedFile, File


from django.contrib import messages
from django.shortcuts import redirect

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UploadedFile, File

def fileupload(request):
    if request.method == 'POST':
        uploaded_files = request.FILES.getlist('files')
        
        # Assuming you have a User model and are using authentication
        # If not, replace this with the appropriate user identification logic
        if request.user.is_authenticated:
            uploaded_file_instance = UploadedFile.objects.create(user=request.user)
            
            for uploaded_file in uploaded_files:
                file_instance = File.objects.create(uploaded_file=uploaded_file_instance, file=uploaded_file)
            
            messages.info(request, 'File uploaded successfully')
            return redirect('fileupload')
        else:
            messages.error(request, 'You must be logged in to upload files.')
            return redirect('signin')  # Redirect to login page if user is not authenticated

    return render(request, 'home.html')  # Assuming you have a template named 'fileupload.html'

    
    




   


