from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.conf import settings
import json
import slack
from randr.models import ChatChannel, ChatMessage

@csrf_exempt
def event_handler(request):
    """
    Returns a response with the challenge value.
    """
    if request.method != 'POST':
        return HttpResponse(status=403)

    if request.method == 'POST':
        json_data = json.loads(request.body)
        if json_data['token'] != settings.SLACK_VERIFICATION_TOKEN:
            return HttpResponse(status=403)

        client = slack.WebClient(token=settings.SLACK_BOT_TOKEN)

        if json_data['type'] == 'url_verification':
            response_data = {}
            response_data['challenge'] = json_data['challenge']
            return JsonResponse(response_data)

        event_data = json_data['event']
        channel_id = event_data['channel']
        headline = 'xxx'
        ts = event_data['ts']
        data = event_data['text']
        user = event_data['user']
        if 'bot_id' in event_data:
            return HttpResponse(status=200)

        if json_data['type'] == 'event_callback':
            try:
                c = ChatChannel.objects.get(channel_id=channel_id)
            except Exception as e:
                try:
                    c = ChatChannel.objects.create(channel_id=channel_id, headline=headline)
                except Exception as e:
                    print(e)
                    return HttpResponse(status=500)
            # save to db
            m = ChatMessage(ts=ts, data=data)
            m.channel = c
            m.save()

            # response in slack
            response_msg = ":wave:, Hello <@%s>, Noted" % user
            client.chat_postMessage(channel=channel_id, text=response_msg)
            return HttpResponse(status=200)

        else:
            return HttpResponse(status=200)