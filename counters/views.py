from django.http import HttpResponse
from django.db.models import F
from .models import Counter


def counter(request, slug):
    Counter.objects.get_or_create(slug=slug)
    Counter.objects.filter(slug=slug).update(count=F("count") + 1)
    return HttpResponse(Counter.objects.get(slug=slug).count, content_type="text/plain")


def hello_word(request):
    return HttpResponse("Hello World!", content_type="text/plain")
