from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import os

# Create your views here.
def index(request):
    print(os.listdir())
    template = loader.get_template('index.html')
    context ={'grow_light':{'on':'No', 'hours_left':'9'}}
    return HttpResponse(template.render(context,request))