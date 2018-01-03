# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name='game'

urlpatterns = [
    # ex: /game/  
    url(r'^$', views.index, name='index'),
    # ex: /game/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /game/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /game/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    
     

    
     #ex: /game/1/    
#    url(r'^game/(?P<game_id>[0-9]+)/$', views.gamesp, name='gamesp'),
#    url(r'^game/(?P<game_id>[0-9]+)/$', views.gamejin, name='gamejin'),
    url(r'^game/gamesp/', views.gamesp, name='gamesp'),
    url(r'^game/gamejin/', views.gamejin, name='gamejin'),
#    url(r'^game/gametensor/', views.gametensor, name='gametensor'),
    url(r'^game/gametensor/(?P<num1>\d+)/(?P<num2>\d+)/$',views.gametensor, name='gametensor'),

# url(r'^game/', include('game.urls')),
  
]
