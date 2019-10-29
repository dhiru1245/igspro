from django.shortcuts import render
from .forms import ContactForm,FeedbackForm
from .models import ContactData,Service,FeedbackData,ImageData,GraphData
from chartit import DataPool,Chart


from django import template
#from django.utils import simplejson
import simplejson
from django.utils.safestring import mark_safe


from django.shortcuts import render_to_response
import random
import datetime
import time



def home(request):
    return render(request,'home.html')


def contact(request):
    if request.method == "POST":
        cfarm = ContactForm(request.POST)
        if cfarm.is_valid():
            name = request.POST.get('name','')
            add = request.POST.get('add','')
            email = request.POST.get('email','')
            mob = request.POST.get('mob','')

            data = ContactData(
                name = name,
                add = add,
                email = email,
                mob = mob,


            )
            data.save()
            cfarm = ContactForm()
            return render(request,'contact.html',{'cfarm':cfarm})
    else:
        cfarm = ContactForm()


        return render(request,'contact.html',{'cfarm':cfarm})

def feedback(request):
    if request.method == "POST":
        aform = FeedbackForm(request.POST)
        if aform.is_valid():
            name = request.POST.get('name','')
            rating = request.POST.get('rating','')
            feedback = request.POST.get('feedback','')
            time = request.POST.get('time','')

            name = name.capitalize()

            data = FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                time = time,

            )
            data.save()
            aform = FeedbackForm()
            return render(request,'feedback.html',{'aform':aform})


    else:

        aform = FeedbackForm()
        x = FeedbackData.objects.all()
        return render(request,'feedback.html',{'aform':aform, 'x':x})




def gallary(request):
    img = ImageData.objects.all()
    return render(request,'gallary.html',{'img':img})

def services(request):

    serv =  Service.objects.all()
    return render(request,'services.html',{'serv':serv})


def graph(request):
    graph = \
       DataPool(
           series=
           [{'options':{
               'source':GraphData.objects.all()},
               'terms':[
                 'block_name',
                   'yf',
                   'awc',
               'cc',]}
           ])
    #create the chart object
    cht = Chart(
        datasource= graph,
        series_options=
        [{'options':{
            'type':'column',
            'stacking': False},
            'terms':{
                'block_name':[
                    'block_name',
                    'yf',
                    'awc',
                'cc']

        }}],
        chart_options =
        {'title':{
            'text': 'Total complete work'},
            'xAxis':{
                'title':{
                    'text':'work done'}}})
    return render(request,'Report.html',{'cht':cht})















