from django.conf import settings
from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

from apps.payouts import views

urlpatterns = patterns('',
    #url(r"^$", direct_to_template, {"template": "about/about.html"}, name="what_next"),
    url(r'^$', views.IndexView.as_view(), name='index_payouts'),
)
