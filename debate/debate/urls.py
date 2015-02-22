from django.conf.urls import patterns, include, url
from debate.base.views import DebateView
from debate.base.views import (
    DendogramView, NetworkVisualizerAfterView, NetworkVisualizerBeforeView,
    NetworkVisualizerSolutionsAfter1View, NetworkVisualizerSolutionsBefore1View,
    VetoFinalView, RegionsView, Index
)

urlpatterns = patterns(
    '',
    url(r'^debate/(?P<title>[\w-]+)-(?P<id>[0-9]+)$',
        DebateView.as_view(), name='debate'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^dendogram$', DendogramView.as_view()),
    url(r'^network-before$', NetworkVisualizerBeforeView.as_view()),
    url(r'^network-after$', NetworkVisualizerAfterView.as_view()),
    url(r'^network-solutions-before$',
        NetworkVisualizerSolutionsBefore1View.as_view()),
    url(r'^network-solutions-after$',
        NetworkVisualizerSolutionsAfter1View.as_view()),
    url(r'^regions$', RegionsView.as_view()),
    url(r'^veto$', VetoFinalView.as_view()),
    url(r'^$', Index.as_view()),
)
