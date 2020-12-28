from django.shortcuts import render,redirect

# Create your views here.
def index(request):
   return render(request, "index.html")

def james_consult(request):
    return render(request, "james_consult.html")

def about_me(request):
    return render(request, "about_me.html")