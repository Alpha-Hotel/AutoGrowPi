from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import os
from forms import AlarmForm
import text_messaging

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
        'ambient_data':{
            'temperature': 75,
            'tempurature_24_low': 60,
            'temperature_24_high':80,
            'light_level': 30,
        },
        'nutrients':{
            'level':50,
            'alarm':10,
        },
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

def config(request):
    if request.method == "POST":
        form = AlarmForm(request.POST)
        print(request.POST.__getitem__("cellphone"), request.POST.__getitem__("cellphone_carrier"))
        text_messaging.test_message(request.POST.__getitem__("cellphone"), request.POST.__getitem__("cellphone_carrier"))
        return HttpResponseRedirect("/")
    else:
        form = AlarmForm()
        return render(request, "config.html", {'form':form})