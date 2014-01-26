from django.conf import settings
from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

from apps.stats import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index_stats'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^player/(?P<pk>\d+)/$', views.PlayerInfoView.as_view(), name='playerinfo'),
)
