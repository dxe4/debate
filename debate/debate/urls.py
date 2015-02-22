from django.conf.urls import patterns, include, url
from debate.base.views import DebateView


urlpatterns = patterns(
    '',
    url(r'^debate/(?P<title>[\w-]+)-(?P<id>[0-9]+)$',
        DebateView.as_view(), name='debate'),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
