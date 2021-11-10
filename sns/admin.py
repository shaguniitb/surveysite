from django.contrib import admin
from .models import Comment, Participant, ToggleSetting, WordFilterSetting, IntensitySliderSetting, ProportionSliderSetting

# Register your models here.

admin.site.register(Comment)
admin.site.register(Participant)
admin.site.register(ToggleSetting)
admin.site.register(WordFilterSetting)
admin.site.register(IntensitySliderSetting)
admin.site.register(ProportionSliderSetting)
