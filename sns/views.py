from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, reverse
from django.template.loader import render_to_string
from django.template import RequestContext
from .models import Participant, ToggleSetting, WordFilterSetting, IntensitySliderSetting
from .forms import WfForm, IntensitySliderForm
import json

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the sns index.")

def feed(request):
    return render(request, "sns/feed.html", {})


def toggle(request):
    participant = Participant.objects.get(id = 1)
    toggleSetting, _ = ToggleSetting.objects.get_or_create(participant = participant)    
    if request.method =='POST':
        post_value = request.POST['filter_toxic']
        toggleSetting.filter_toxic = post_value == 'true'
        toggleSetting.save()
        response = {
            'message': 'Your changes have been saved.'
        }
        return HttpResponse(json.dumps(response), content_type='application/json')
    else: 
        return render(request, "sns/toggle.html", {'toggleSetting': toggleSetting})    

def wordfilter(request):
    participant = Participant.objects.get(id = 1)
    wfSetting, _ = WordFilterSetting.objects.get_or_create(participant = participant)    

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WfForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            word_filters = form.cleaned_data['word_filters']
            wfSetting.word_filters = word_filters
            wfSetting.save()
            response = {
                'message': 'Your changes have been saved.'
            }

            return HttpResponse(json.dumps(response), content_type='application/json')

    else: 
        form = WfForm(initial={'word_filters': wfSetting.word_filters})
        return render(request, "sns/wordfilter.html", {'form': form})    


def int_slider(request):
    participant = Participant.objects.get(id = 1)
    sliderSetting, _ = IntensitySliderSetting.objects.get_or_create(participant = participant)    

    if request.method == 'POST':
        form = IntensitySliderForm(request.POST)
        if form.is_valid():
            slider_level = form.cleaned_data['slider_level']
            sliderSetting.slider_level = slider_level
            sliderSetting.save()
            response = {
                'message': 'Your changes have been saved.'
            }

            return HttpResponse(json.dumps(response), content_type='application/json')

    else: 
        form = IntensitySliderForm(initial={'slider_level': sliderSetting.slider_level})
        return render(request, "sns/int_slider.html", {'form': form})    