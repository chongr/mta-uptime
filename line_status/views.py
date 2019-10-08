import datetime

from django.http import JsonResponse
from django.utils.timezone import utc
from line_status.models import LineStatus


def get(request, **kwargs):
    return JsonResponse(
        LineStatus.objects.get(line_name=kwargs['line_name']).to_json()
    )


def get_delayed_time(request, **kwargs):
    line = LineStatus.objects.get(line_name=kwargs['line_name'])
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    timediff = now - line.created_at
    total_time = timediff.total_seconds()
    delayed_time = line.get_delayed_time()
    uptime_fraction = 1 - (delayed_time / total_time)
    return JsonResponse({
        "line_name": line.line_name,
        "uptime_fraction": uptime_fraction
    })
