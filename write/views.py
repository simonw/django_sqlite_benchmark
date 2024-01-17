from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from .models import Row


@csrf_exempt
def write_row_from_json(request):
    if request.method == "POST":
        data = request.POST
        row = Row(
            name=data["name"],
            campaign=data["campaign"],
            voice=data["voice"],
            recognize=data["recognize"],
            inside=data["inside"],
            growth=data["growth"],
            side=data["side"],
            yard=data["yard"],
            discussion=data["discussion"],
        )
        row.save()
        # Return JSON of row
        return JsonResponse(row.to_json())
    else:
        return HttpResponse("Not allowed", status=405)


@csrf_exempt
@transaction.atomic()
def write_row_after_read_from_json(request):
    Row.objects.filter().first()  # Do a read query before the write
    if request.method == "POST":
        data = request.POST
        row = Row(
            name=data["name"],
            campaign=data["campaign"],
            voice=data["voice"],
            recognize=data["recognize"],
            inside=data["inside"],
            growth=data["growth"],
            side=data["side"],
            yard=data["yard"],
            discussion=data["discussion"],
        )
        row.save()
        # Return JSON of row
        return JsonResponse(row.to_json())
    else:
        return HttpResponse("Not allowed", status=405)
