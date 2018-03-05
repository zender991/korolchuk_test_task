from django.shortcuts import render
from pyzipcode import ZipCodeDatabase


def index(request):
    return render(request, 'zip_codes/index.html')


def get_coordinates(request):
    zcdb = ZipCodeDatabase()
    try:
        zipcode = zcdb[request.POST.get('zip_code')]
        coordinates = {
            'zip_code': zipcode.zip,
            'longitude': zipcode.longitude,
            'latitude': zipcode.latitude
        }
        context = {'coordinates': coordinates}
    except Exception as e:
        context = {'error': e}

    return render(request, 'zip_codes/coordinates.html', context)
