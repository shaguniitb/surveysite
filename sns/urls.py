from django.urls import path

from . import views, create_tables

app_name = 'sns'
urlpatterns = [
    path('', views.is_new_user, name='is_new_user'),
    path('get_user', views.get_user, name='get_user'),
    path('interface', views.interface, name='interface'),
    path('settings', views.settings, name='settings'),
    path('feed', views.feed, name='feed'),
    path('toggle', views.toggle, name='toggle'),
    path('wordfilter', views.wordfilter, name='wordfilter'),
    path('slider', views.semantic_slider, name='semantic_slider'),
    path('create_tables', create_tables.create_tables),
]