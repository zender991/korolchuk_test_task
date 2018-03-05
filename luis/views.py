from django.shortcuts import render
from luis.credentials import luis_api_key, luis_url
from logging.handlers import TimedRotatingFileHandler
import logging
import requests


formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

handler = TimedRotatingFileHandler('logs/app.log', when="midnight", interval=1)
handler.setFormatter(formatter)

logger = logging.getLogger("LuisApp")
handler.suffix = "%Y-%m-%d.log"
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def get_luis_answer(request):
    headers = {
        'Ocp-Apim-Subscription-Key': luis_api_key,
    }

    params = {
        'q': request.POST.get('luis_query'),
        'timezoneOffset': '0',
        'verbose': 'false',
        'spellCheck': 'false',
        'staging': 'false',
    }

    try:
        logger.info("Sent query to LUIS - " + request.POST.get('luis_query'))
        r = requests.get(luis_url, headers=headers, params=params)
        json_response = r.json()
        logger.info("Response from LUIS - " + str(json_response['topScoringIntent']['intent']))
        context = {'intent': json_response}

    except Exception as e:
        context = {'error': e}
        logger.error(e)

    return render(request, 'luis/luis_answer.html', context)
