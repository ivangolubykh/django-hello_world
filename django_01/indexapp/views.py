from django.shortcuts import render, render_to_response

# Create your views here.

def index(request):
    return render_to_response("index.html")

def learn(request):
    return render_to_response("learn.html")

def work(request):
    return render_to_response("work.html")
