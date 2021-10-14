from django.contrib import admin
from .models import Comment, Interface, Participant, ToggleSetting, WordFilterSetting

# Register your models here.

admin.site.register(Comment)
admin.site.register(Interface)
admin.site.register(Participant)
admin.site.register(ToggleSetting)
admin.site.register(WordFilterSetting)
