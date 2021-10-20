from django import forms

from .widgets import RangeInput
from .models import Participant, WordFilterSetting, SliderSetting


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

class SliderForm(forms.ModelForm):
  slider_level = forms.IntegerField(widget = RangeInput)

  class Meta:
    model = SliderSetting
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
