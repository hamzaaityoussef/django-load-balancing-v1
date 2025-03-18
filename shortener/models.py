from django.db import models
from django.db import connection

class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shortener_shortenedurl'
        indexes = [
            models.Index(fields=['short_code']),
        ]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        connection.close()  # Explicitly close connection after save

    @classmethod
    def get_by_short_code(cls, short_code):
        try:
            url = cls.objects.get(short_code=short_code)
            connection.close()  # Close connection after read
            return url
        except cls.DoesNotExist:
            connection.close()
            return None