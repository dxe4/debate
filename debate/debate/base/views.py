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
