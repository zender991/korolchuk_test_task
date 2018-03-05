from django.conf.urls import url
from zip_codes.views import index, get_coordinates


app_name = 'zip_codes'
urlpatterns = [
    url(r'^get-coordinates/$', get_coordinates, name='get-coordinates')
]