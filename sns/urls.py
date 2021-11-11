from django.urls import path

from . import views, create_tables

app_name = 'sns'
urlpatterns = [
    path('', views.register, name='register'),
    path('login', views.login, name='login'),
    path('interface', views.interface, name='interface'),
    path('settings', views.settings, name='settings'),
    path('feed', views.feed, name='feed'),
    path('toggle', views.toggle, name='toggle'),
    path('wordfilter', views.wordfilter, name='wordfilter'),
    path('intensity_slider', views.intensity_slider, {'with_examples': False}, name='intensity_slider'),
    path('intensity_slider/with_examples', views.intensity_slider, {'with_examples': True}, name='intensity_slider_with_examples'),
    path('proportion_slider', views.proportion_slider, {'with_examples': False}, name='proportion_slider'),
    path('proportion_slider/with_examples', views.proportion_slider, {'with_examples': True}, name='proportion_slider_with_examples'),
    path('create_tables', create_tables.create_tables),
]
