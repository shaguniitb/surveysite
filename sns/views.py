from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, reverse
from django.template.loader import render_to_string
from django.template import RequestContext
from .models import Comment, Participant, ToggleSetting, WordFilterSetting, SliderSetting
from .forms import WfForm, SliderForm, InterfaceForm
import json, re

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the sns index.")

def get_matched_comment_ids(word_filters):
    comments = Comment.objects.all()
    if (word_filters == '' or word_filters is None):
        return [comment.id for comment in comments]
    matched_comment_ids = []
    for comment in comments:
        lookups = []
        rules = word_filters.strip().split(',')
        for rule in rules:
            rule = rule.strip()
            lookup = re.search(r'\b({})\b'.format(rule), comment.text, re.IGNORECASE)
            lookups.append(lookup)
        if any(lookups):
            matched_comment_ids.append(comment.id)  
    return matched_comment_ids

def interface(request):
    participant = Participant.objects.get(id = 1)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InterfaceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            setting = form.cleaned_data['setting']
            participant.setting = setting
            participant.save()
            if (setting == "1"):
                return HttpResponseRedirect(reverse('sns:toggle'))
            elif (setting == "2"):
                return HttpResponseRedirect(reverse('sns:wordfilter'))  
            elif (setting == "3"):
                return HttpResponseRedirect(reverse('sns:int_slider'))                                

    else:
        form = InterfaceForm(initial={'setting': participant.setting})
        return render(request, "sns/interface.html", {'form': form})    

def feed(request):
    participant = Participant.objects.get(id = 1)
    if (participant.setting == "1"):
        participant.resetWordFilter()
        participant.resetSlider()
        toggleSetting, _ = ToggleSetting.objects.get_or_create(participant = participant)
        filter_toxic = toggleSetting.filter_toxic
        if (filter_toxic):
            comments = Comment.objects.filter(perspective_score__lte = 0.8)
        else:
            comments = Comment.objects.all()

    elif (participant.setting == "2"):
        participant.resetToggle()
        participant.resetSlider()        
        wordFilterSetting, _ = WordFilterSetting.objects.get_or_create(participant = participant)
        word_filters = wordFilterSetting.word_filters
        matched_comment_ids = get_matched_comment_ids(word_filters)
        comments = Comment.objects.exclude(id__in = matched_comment_ids)

    elif (participant.setting == "3"):
        participant.resetToggle()
        participant.resetWordFilter()  
        sliderSetting, _ = SliderSetting.objects.get_or_create(participant = participant)
        slider_level = sliderSetting.slider_level
        if (slider_level == 1):
            comments = Comment.objects.all()
        elif (slider_level == 2):
            comments = Comment.objects.filter(perspective_score__lte = 0.8)                    
        elif (slider_level == 3):
            comments = Comment.objects.filter(perspective_score__lte = 0.6)
        elif (slider_level == 4):
            comments = Comment.objects.filter(perspective_score__lte = 0.4)
        elif (slider_level == 5):
            comments = Comment.objects.filter(perspective_score__lte = 0.2)                                                        
    return render(request, "sns/feed.html", {'comments': comments})


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
    sliderSetting, _ = SliderSetting.objects.get_or_create(participant = participant)

    if request.method == 'POST':
        form = SliderForm(request.POST)
        if form.is_valid():
            slider_level = form.cleaned_data['slider_level']
            sliderSetting.slider_level = slider_level
            sliderSetting.save()
            response = {
                'message': 'Your changes have been saved.'
            }

            return HttpResponse(json.dumps(response), content_type='application/json')

    else:
        form = SliderForm(initial={'value': sliderSetting.slider_level})
        return render(request, "sns/int_slider.html", {'form': form})
