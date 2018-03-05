from django.shortcuts import render
from luis.credentials import luis_api_key, luis_url
import requests


def get_luis_answer(request):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': luis_api_key,
    }

    params = {
        # Query parameter
        'q': request.POST.get('luis_query'),
        # Optional request parameters, set to default values
        'timezoneOffset': '0',
        'verbose': 'false',
        'spellCheck': 'false',
        'staging': 'false',
    }

    try:
        r = requests.get(luis_url, headers=headers, params=params)
        context = {'intent': r.json()}

    except Exception as e:
        context = {'error': e}

    return render(request, 'luis/luis_answer.html', context)
