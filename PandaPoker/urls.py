from django.conf import settings
from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

#from pinax.apps.account.openid_consumer import PinaxConsumer

handler500 = "pinax.views.server_error"


urlpatterns = patterns("",
    url(r"^$", direct_to_template, {
        "template": "homepage.html",
    }, name="home"),
    url(r"^admin/invite_user/$", "pinax.apps.signup_codes.views.admin_invite_user", name="admin_invite_user"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("pinax.apps.account.urls")),
    url(r"^about/", include("about.urls")),
    url(r"^profiles/", include("profiles.urls", namespace="profiles")),
    url(r"^variations/", include("variations.urls", namespace="variations")),
    url(r"^stats/", include("stats.urls", namespace="stats")),
    url(r"^payouts/", include("payouts.urls", namespace="payouts")),
    #url(r"^openid/", include(PinaxConsumer().urls)),   
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
