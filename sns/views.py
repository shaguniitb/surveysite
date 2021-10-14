from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, reverse
from django.template.loader import render_to_string
from django.template import RequestContext
from .models import Participant, ToggleSetting, WordFilterSetting
from .forms import WfForm
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
        form = WfForm()
        return render(request, "sns/wordfilter.html", {'form': form})    


def slider(request):
    return render(request, "sns/slider.html", {})        