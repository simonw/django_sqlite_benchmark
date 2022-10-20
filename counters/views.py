from django.http import HttpResponse
from .models import Counter


def counter(request, slug):
    counter = Counter.objects.get_or_create(slug=slug)[0]
    counter.count += 1
    counter.save()
    return HttpResponse(counter.count, content_type="text/plain")
