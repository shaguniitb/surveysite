from django import forms

from .widgets import RangeInput
from .models import WordFilterSetting, SliderSetting


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
