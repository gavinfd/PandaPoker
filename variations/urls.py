from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

from variations import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index_variation'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)