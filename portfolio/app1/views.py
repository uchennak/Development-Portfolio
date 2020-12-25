from django.shortcuts import render,redirect

# Create your views here.
def index(request):
   return render(request, "index.html")

def show_java(request):
    return render(request, "java_projects.html")

def show_python(request):
    pass

def about_me(request):
    return render(request, "about_me.html")