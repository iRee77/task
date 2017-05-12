import random
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
#    return HttpResponse('Йо, собаки')
    number = random.randrange(0, 100)

    context = {
        'value': 'НАРУТО1',
        'number': str(number),
    }
    return render(request, 'index.html', context)

def p_median(request):
    context = {
        'zmaps': 'https://zmaps.googleapis.com/zmaps/api/directions/json?origin=75+9th+Ave+New+York,+NY&destination=MetLife+Stadium+1+MetLife+Stadium+Dr+East+Rutherford,+NJ+07073&key=AIzaSyD_63p4S9oIe3nrwGekn1FBLuReTMH3sgg'

    }
    return render(request, 'p_median.html', context)

#AIzaSyCLkE1tkBbGoV4wn7vhs2neqJUPl6sAbN0 второй

#AIzaSyD_63p4S9oIe3nrwGekn1FBLuReTMH3sgg