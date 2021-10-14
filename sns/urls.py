from django.urls import path

from . import views, create_tables

urlpatterns = [
    path('', views.index, name='index'),
    path('feed', views.feed, name='feed'),
    path('toggle', views.toggle, name='toggle'),
    path('wordfilter', views.wordfilter, name='wordfilter'),
    path('int_slider', views.int_slider, name='int_slider'),
    path('create_tables', create_tables.create_tables),
]
