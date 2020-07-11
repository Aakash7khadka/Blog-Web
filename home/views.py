from django.shortcuts import render
from django.http import HttpResponse
from .models import Post 



# Create your views here.
def home(request):
    return render(request,'home/home.html',{'posts':Post.objects.all(),'title':'Home'})
def about(request):
    return render(request,'home/about.html',{'title':'About'})