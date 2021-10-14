from django import forms
from .models import WordFilterSetting

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