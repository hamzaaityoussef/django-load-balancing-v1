import random, string
from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortenedURL

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def shorten_url(request):
    if request.method == "POST":
        original_url = request.POST.get('url')
        short_code = generate_short_code()
        short_url = ShortenedURL.objects.create(original_url=original_url, short_code=short_code)
        return render(request, "shortener/result.html", {"short_url": short_url})
    return render(request, "shortener/index.html")

def redirect_url(request, short_code):
    url_entry = get_object_or_404(ShortenedURL, short_code=short_code)
    return redirect(url_entry.original_url)
