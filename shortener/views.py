def generate_short_code(length=6):
    import random, string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache  # Add this
from .models import ShortenedURL    # Add this

class APIShortenURL(APIView):
    def post(self, request):
        original_url = request.data.get("url")
        if not original_url:
            return Response({"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST)

        cached_code = cache.get(f"url:{original_url}")
        if cached_code:
            short_code = cached_code
        else:
            short_code = generate_short_code()
            ShortenedURL.objects.create(original_url=original_url, short_code=short_code)
            cache.set(f"url:{original_url}", short_code, timeout=86400)
            cache.set(f"short:{short_code}", original_url, timeout=86400)

        return Response({"short_url": f"http://localhost:8080/shortener/{short_code}"}, status=status.HTTP_201_CREATED)

class APIExpandURL(APIView):
    def get(self, request, short_code):
        original_url = cache.get(f"short:{short_code}")
        if not original_url:
            url_entry = ShortenedURL.objects.filter(short_code=short_code).first()
            if not url_entry:
                return Response({"error": "Short URL not found"}, status=status.HTTP_404_NOT_FOUND)
            original_url = url_entry.original_url
            cache.set(f"short:{short_code}", original_url, timeout=86400)

        return Response({"original_url": original_url}, status=status.HTTP_200_OK)
