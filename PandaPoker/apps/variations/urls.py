from django.conf import settings
from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

from apps.variations import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index_variations'),
    #url(r'add/$', views.AddView.as_view(), name='add_variation'),
    #url(r'outline/$', views.outline, name='outline_variation'),
)
