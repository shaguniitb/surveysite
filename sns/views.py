from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the sns index.")

def feed(request):
    return render(request, "sns/feed.html", {})