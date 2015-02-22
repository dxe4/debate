from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView

from debate.base.models import Debate, Comment

from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('text',)


class DebateView(TemplateView):
    template_name = 'debate.html'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        pk = kwargs['id']
        debate = get_object_or_404(
            Debate.objects.select_related(
                'solutions', 'solutions__comment'
            ),
            pk=pk
        )

        solutions = list(debate.solutions.all())
        comments = [
            (count, solution.all_comments())
            for count, solution in enumerate(solutions)
        ]
        return {
            'debate': debate,
            'solutions': solutions,
            'comments': comments,
        }


class CreateTag(ListCreateAPIView):
    model = Comment
    serializer_class = Comment

    def post(self, request, *args, **kwargs):
        print(args, kwargs)
        return self.create(request, *args, **kwargs)


class DendogramView(TemplateView):
    template_name = 'Dendrogram.html'
    http_method_names = ['get']


class NetworkVisualizerBeforeView(TemplateView):
    template_name = 'NetworkVisualizerBefore.html'
    http_method_names = ['get']


class NetworkVisualizerAfterView(TemplateView):
    template_name = 'NetworkVisualizerAfter.html'
    http_method_names = ['get']


class NetworkVisualizerSolutionsBefore1View(TemplateView):
    template_name = 'NetworkVisualizerSolutionsBefore1.html'
    http_method_names = ['get']


class NetworkVisualizerSolutionsAfter1View(TemplateView):
    template_name = 'NetworkVisualizerSolutionsAfter1.html'
    http_method_names = ['get']


class RegionsView(TemplateView):
    template_name = 'regions.html'
    http_method_names = ['get']


class VetoFinalView(TemplateView):
    template_name = 'veto_final.html'
    http_method_names = ['get']


class Index(TemplateView):
    template_name = 'index.html'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        urls = [
            'dendogram',
            'network-before',
            'network-after',
            'network-solutions-before',
            'network-solutions-after',
            'regions',
            'veto',
        ]
        return {
            'urls': urls
        }
