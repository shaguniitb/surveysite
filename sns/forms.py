from django import forms
from .models import WordFilterSetting, IntensitySliderSetting

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
        fields = [ "word_filters"]    

class IntensitySliderForm(forms.ModelForm):
    slider_level = forms.CharField(
        widget=forms.RadioSelect(
            choices=IntensitySliderSetting.SLIDER_CHOICES,
            attrs={
            "class": "slider-input",
            }            
        )
    )

    class Meta:
        model = IntensitySliderSetting
        fields = [ "slider_level"]            