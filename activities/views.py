from django.shortcuts import render
from django.views import generic
from calls.models import Call


class TestView(generic.TemplateView):
    template_name = "tests.html"

class HistoryView(generic.ListView):
    template_name = "history-test.html"
    model = Call
    context_object_name = 'call'
    queryset = Call.objects.all()

    today_calls = Call.objects.get

    def get_context_data(self, **kwargs):
        context = super(RelatorioView, self).get_context_data(**kwargs)
        context.update({
            'group_list': self.group_list,
            'setor_list': self.setor_list,
            'concessionaria_list':self.concessionaria_list,
            'pagamento_list':self.pagamento_list
        })
        return context
