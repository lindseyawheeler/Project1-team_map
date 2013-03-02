# app urls team/urls.py
from django.conf.urls.defaults import patterns, url

from team import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='team_home'),
    url(r'^roster/$', views.rosterList, name='team_roster_list'),
    url(r'^players/$', views.playersList, name='team_players_list'),
    url(r'^roster/(?P<pk>\d+)$', views.roster, name='team_roster'),
    url(r'^players/(?P<pk>\d+)$', views.players, name='team_players'),
    )

