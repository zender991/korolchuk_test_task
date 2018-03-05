from django.shortcuts import render
import requests


def get_luis_answer(request):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': 'b226f724821f4262a3617aa1b6723ca0',
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
        r = requests.get('https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/69d4408b-8d1d-4a9f-b70b-02aa40163378', headers=headers, params=params)
        context = {'intent': r.json()}

    except Exception as e:
        context = {'error': e}

    return render(request, 'luis/luis_answer.html', context)
