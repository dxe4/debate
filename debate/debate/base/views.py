from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from debate.base.models import Debate


class DebateView(TemplateView):
    template_name = 'debate.html'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        pk = kwargs['id']
        debate = get_object_or_404(
            Debate.objects.select_related('solutions'), pk=pk
        )
        print(debate.solutions.all())
        return {
            'debate': debate,
            'solutions': debate.solutions.all()
        }
