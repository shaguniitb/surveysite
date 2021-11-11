from django import forms
from .widgets import SemanticScale
from .models import Participant, WordFilterSetting, IntensitySliderSetting, ProportionSliderSetting

class LoginForm(forms.Form):
  action = forms.CharField(
    required = False,
    widget=None
  )

class ParticipantForm(forms.ModelForm):
  id = forms.CharField()
  class Meta:
    model = Participant
    fields = [ "id", "username", "turker_id" ]


class WfForm(forms.ModelForm):
  word_filters = forms.CharField(
    required=False,
    widget=forms.Textarea(
      attrs={
      "placeholder": "Eg. Apple, Orange, Pear",
      "class": "textFilter-input",
      }
    ),
  )

  class Meta:
    model = WordFilterSetting
    fields = [ "word_filters" ]

class IntensitySliderForm(forms.ModelForm):
  slider_level = forms.IntegerField(
    widget = SemanticScale,
    max_value = 5,
    min_value = 1
  )

  class Meta:
    model = IntensitySliderSetting
    fields = [ "slider_level" ]

class ProportionSliderForm(forms.ModelForm):
  slider_level = forms.IntegerField(
    widget = SemanticScale,
    max_value = 5,
    min_value = 1
  )

  class Meta:
    model = ProportionSliderSetting
    fields = [ "slider_level" ]

class InterfaceForm(forms.ModelForm):
  setting = forms.CharField(
    widget=forms.RadioSelect(
      choices = Participant.INTERFACE_CHOICES
    ),
  )

  class Meta:
    model = Participant
    fields = [ "setting" ]
