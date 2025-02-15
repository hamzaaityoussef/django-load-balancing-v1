import socket
from django.http import HttpResponse
from django.shortcuts import render 

def home(request):
    hostname = socket.gethostname()
    return render(request, "home.html", {"hostname": hostname})
