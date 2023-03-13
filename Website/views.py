from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import os

test = {'grow_light':
            {'on':'No', 
            'daylight_hours':10,
            'hours_left':'9', 
            'lumens':0}, 
        'soil_moisture':
            {"average":65, 
            'low':45,
            'high':85, 
            'time':'Wed March 4 at 12:35 MDT', 
            'tank_level':55},
        'rpi_status':{
            'uptime':127,
            'cpu': 35
        }
        }

# Create your views here.
def index(request):
    print(os.listdir())
    template = loader.get_template('index.html')
    context = test
    return HttpResponse(template.render(context,request))