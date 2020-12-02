from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json

from randr.models import ChatChannel, ChatMessage

@csrf_exempt
def event_handler(request):
    """
    Returns a response with the challenge value.
    """
    if request.method == 'POST':
        json_data = json.loads(request.body)

        if json_data['type'] == 'url_verification':
            response_data = {}
            response_data['challenge'] = json_data['challenge']
            return JsonResponse(response_data)

        if json_data['type'] == 'event_callback':
            event_data = json_data['event']
            channel_id = event_data['channel']
            headline = 'xxx'
            ts = event_data['ts']
            data = event_data['text']
            try:
                c = ChatChannel.objects.get(channel_id=channel_id)
            except Exception as e:
                try:
                    c = ChatChannel.objects.create(channel_id=channel_id, headline=headline)
                except Exception as e:
                    print(e)
                    return HttpResponse(status=500)
            m = ChatMessage(ts=ts, data=data)
            m.channel = c
            m.save()
            return HttpResponse(status=200)
