from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, reverse
from django.template.loader import render_to_string
from django.template import RequestContext
from .models import Comment, Participant, ToggleSetting, WordFilterSetting, IntensitySliderSetting, ProportionSliderSetting
from .forms import WfForm, IntensitySliderForm, ProportionSliderForm, InterfaceForm, ParticipantForm
import json, re

# Create your views here.
MAX_COMMENTS = 30

def register(request):
  if request.method == 'POST':
    action = request.POST.get('action', '')
    if action == 'New User':
      participant = Participant.objects.create()
      request.session['participant_id'] = participant.id
      return HttpResponseRedirect(reverse('sns:feed'))
    elif action == 'Existing User':
      return HttpResponseRedirect(reverse('sns:login'))
  # form = LoginForm()
  return render(request, "sns/is_new_user.html", {'uid': '?'})

def login(request):
  if request.method == 'POST':
    form = ParticipantForm(request.POST)
    if form.is_valid():
      if ('id' in form.cleaned_data):
        participant_id = form.cleaned_data['id']
        participant = Participant.objects.get(id = participant_id)
        request.session['participant_id'] = participant.id
        return HttpResponseRedirect(reverse('sns:feed'))
      else:
        return HttpResponseRedirect(reverse('sns:login'))
  form = ParticipantForm()
  return render(request, "sns/get_user.html", {'form': form, 'uid': '?'})

def getParticipantFromSession(request):
  try:
    participant = Participant.objects.get(id=request.session['participant_id'])
  except (KeyError, Participant.DoesNotExist):
    participant = None
  return participant

def get_matched_comments(word_filters):
  comments = Comment.objects.all()
  if (not(word_filters == '' or word_filters is None)):
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
    comments = Comment.objects.exclude(id__in = matched_comment_ids)
  if (len(comments) > MAX_COMMENTS):
    comments = comments[:MAX_COMMENTS]
  return comments

def settingsPage(setting):
  if (setting == "1"):
    return HttpResponseRedirect(reverse('sns:toggle'))
  elif (setting == "2"):
    return HttpResponseRedirect(reverse('sns:wordfilter'))
  elif (setting == "3"):
    return HttpResponseRedirect(reverse('sns:intensity_slider'))
  elif (setting == "4"):
    return HttpResponseRedirect(reverse('sns:proportion_slider'))

def interface(request):
  participant = getParticipantFromSession(request)

  if request.method == 'POST':
    # create a form instance and populate it with data from the request:
    form = InterfaceForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
      setting = form.cleaned_data['setting']
      participant.setting = setting
      participant.save()
      return settingsPage(setting)
  else:
    form = InterfaceForm(initial={'setting': participant.setting})
    return render(request, "sns/interface.html", {'form': form, 'uid': participant.id})

def settings(request):
  participant = getParticipantFromSession(request)
  if participant is None:
    return HttpResponseRedirect(reverse('sns:register'))
  setting = participant.setting
  return settingsPage(setting)

def getCommentsFromSets(setList):
  idList = []
  for l in setList:
    idList += [comment.id for comment in l]
  comments = Comment.objects.filter(id__in = idList)
  return comments

def get_slider_comments(slider_type, slider_level):
  if (slider_type == 'intensity'):
    if (slider_level == 1):
      first_set = Comment.objects.filter(toxicity_score__gte = 0.2)
      second_set = Comment.objects.filter(toxicity_score__lt = 0.2)[:10]
      return getCommentsFromSets([first_set, second_set])
    elif (slider_level == 2):
      first_set = Comment.objects.filter(toxicity_score__gte = 0.2, toxicity_score__lt = 0.8)
      second_set = Comment.objects.filter(toxicity_score__lt = 0.2)[:15]
      return getCommentsFromSets([first_set, second_set])
    elif (slider_level == 3):
      first_set = Comment.objects.filter(toxicity_score__gte = 0.2, toxicity_score__lt = 0.6)
      second_set = Comment.objects.filter(toxicity_score__lt = 0.2)[:20]
      return getCommentsFromSets([first_set, second_set])
    elif (slider_level == 4):
      first_set = Comment.objects.filter(toxicity_score__gte = 0.2, toxicity_score__lt = 0.4)
      second_set = Comment.objects.filter(toxicity_score__lt = 0.2)[:25]
      return getCommentsFromSets([first_set, second_set])
    elif (slider_level == 5):
      return Comment.objects.filter(toxicity_score__lt = 0.2)[:30]

  elif (slider_type == 'proportion'):
    if (slider_level == 1):
      first_set = Comment.objects.filter(toxicity_score__gte = 0.2)
      second_set = Comment.objects.filter(toxicity_score__lt = 0.2)[:10]
      return getCommentsFromSets([first_set, second_set])
    elif (slider_level == 2):
      first_set = Comment.objects.filter(toxicity_score__gte = 0.2)[:15]
      second_set = Comment.objects.filter(toxicity_score__lt = 0.2)[:15]
      return getCommentsFromSets([first_set, second_set])
    elif (slider_level == 3):
      first_set = Comment.objects.filter(toxicity_score__gte = 0.2)[:10]
      second_set = Comment.objects.filter(toxicity_score__lt = 0.2)[:20]
      return getCommentsFromSets([first_set, second_set])
    elif (slider_level == 4):
      first_set = Comment.objects.filter(toxicity_score__gte = 0.2)[:5]
      second_set = Comment.objects.filter(toxicity_score__lt = 0.2)[:25]
      return getCommentsFromSets([first_set, second_set])
    elif (slider_level == 5):
      return Comment.objects.filter(toxicity_score__lt = 0.2)[:30]

def feed(request):
  participant = getParticipantFromSession(request)
  if participant is None:
    return HttpResponseRedirect(reverse('sns:register'))
  print ("setting:", participant.setting)
  if (participant.setting == "1"):
    participant.resetWordFilter()
    participant.resetIntensitySlider()
    participant.resetProportionSlider()
    toggleSetting, _ = ToggleSetting.objects.get_or_create(participant = participant)
    filter_toxic = toggleSetting.filter_toxic
    if (filter_toxic):
      comments = Comment.objects.filter(toxicity_score__lt = 0.2)[:MAX_COMMENTS]
    else:
      comments = Comment.objects.all()[:MAX_COMMENTS]
  elif (participant.setting == "2"):
    participant.resetToggle()
    participant.resetIntensitySlider()
    participant.resetProportionSlider()
    wordFilterSetting, _ = WordFilterSetting.objects.get_or_create(participant = participant)
    word_filters = wordFilterSetting.word_filters
    comments = get_matched_comments(word_filters)
  elif (participant.setting == "3"):
    participant.resetToggle()
    participant.resetWordFilter()
    participant.resetProportionSlider()
    sliderSetting, _ = IntensitySliderSetting.objects.get_or_create(participant = participant)
    slider_level = sliderSetting.slider_level
    print ("slider level:", slider_level)
    comments = get_slider_comments('intensity', slider_level)
  elif (participant.setting == "4"):
    participant.resetToggle()
    participant.resetWordFilter()
    participant.resetIntensitySlider()
    sliderSetting, _ = ProportionSliderSetting.objects.get_or_create(participant = participant)
    slider_level = sliderSetting.slider_level
    comments = get_slider_comments('proportion', slider_level)

  return render(request, "sns/feed.html", {'comments': comments, 'uid': participant.id})

def toggle(request):
  participant = getParticipantFromSession(request)
  if participant is None:
    return HttpResponseRedirect(reverse('sns:register'))
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
    return render(request, "sns/toggle.html", {'toggleSetting': toggleSetting, 'uid': participant.id})

def wordfilter(request):
  participant = getParticipantFromSession(request)
  if participant is None:
    return HttpResponseRedirect(reverse('sns:register'))
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
    return render(request, "sns/wordfilter.html", {'form': form, 'uid': participant.id})


def intensity_slider(request, **kwargs):
  with_examples = kwargs['with_examples']
  participant = getParticipantFromSession(request)
  if participant is None:
    return HttpResponseRedirect(reverse('sns:register'))
  sliderSetting, _ = IntensitySliderSetting.objects.get_or_create(participant = participant)
  show_alert = False

  if request.method == 'POST':
    form = IntensitySliderForm(request.POST)
    if form.is_valid():
      slider_level = form.cleaned_data['slider_level']
      sliderSetting.slider_level = slider_level
      sliderSetting.save()
      show_alert = True

  form = IntensitySliderForm(initial = {'slider_level': sliderSetting.slider_level})
  return render(request, "sns/semantic_slider.html", {
    'form': form,
    'uid': participant.id,
    'show_alert': False,
    'slider_mode': 'intensity',
    'with_examples': with_examples,
  })

def proportion_slider(request, **kwargs):
  with_examples = kwargs['with_examples']
  participant = getParticipantFromSession(request)
  if participant is None:
    return HttpResponseRedirect(reverse('sns:register'))

  sliderSetting, _ = ProportionSliderSetting.objects.get_or_create(participant = participant)
  show_alert = False

  # Handle the POST
  if request.method == 'POST':
    form = ProportionSliderForm(request.POST)
    if form.is_valid():
      slider_level = form.cleaned_data['slider_level']
      sliderSetting.slider_level = slider_level
      sliderSetting.save()
      show_alert = True

  form = ProportionSliderForm(initial = {'slider_level': sliderSetting.slider_level})
  return render(request, "sns/semantic_slider.html", {
    'form': form,
    'uid': participant.id,
    'show_alert': show_alert,
    'slider_mode': 'probability',
    'with_examples': with_examples,
  })
