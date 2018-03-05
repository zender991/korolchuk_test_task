from django.conf.urls import url
from luis.views import get_luis_answer


app_name = 'luis'
urlpatterns = [
    url(r'^get-answer/$', get_luis_answer, name='get-luis-answer')
]