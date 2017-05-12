from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import googlemaps
from datetime import datetime

# Последний ключ
#gmaps = googlemaps.Client(key='AIzaSyCtt1pZV6gxM4OPc9qxmlWUyv47bzN0T6I')

# Geocoding an address
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
#now = datetime.now()
#directions_result = gmaps.directions("Sydney Town Hall",
#                                     "Parramatta, NSW",
 #                                    mode="transit",
#                                     departure_time=now)












def p_median(request):
    context = {
        'zmaps': 'https://zmaps.googleapis.com/zmaps/api/directions/json?origin=75+9th+Ave+New+York,+NY&destination=MetLife+Stadium+1+MetLife+Stadium+Dr+East+Rutherford,+NJ+07073&key=AIzaSyD_63p4S9oIe3nrwGekn1FBLuReTMH3sgg'
    }
    return render(request, 'p_median.html', context)


def conftaskpRender(request):
    if request.method == 'GET':
        return render(request, 'conftaskp.html')
    elif request.method == 'POST':
        return conftaskp(request)



def conftaskp(request):
    description = request.POST['description']
    print(description)
    return HttpResponseRedirect("/")

