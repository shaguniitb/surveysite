from django.contrib import admin
from .models import Comment, Interface, Participant

# Register your models here.

admin.site.register(Comment)
admin.site.register(Interface)
admin.site.register(Participant)
