from django.shortcuts import render
from django.views import generic
from calls.models import Call
import datetime



class TestView(generic.TemplateView):
    template_name = "tests.html"

class HistoryView(generic.ListView):
    template_name = "history-agenda.html"
    model = Call
    context_object_name = 'call'
    queryset = Call.objects.all()

    today = datetime.datetime.now()
    yesterday = today -  datetime.timedelta(days=1)

    today_calls = Call.objects.filter(date__year=today.year, 
                                        date__month=today.month,
                                        date__day= today.day)

    yesterday_calls = Call.objects.filter(date__year=yesterday.year, 
                                        date__month=yesterday.month,
                                        date__day= yesterday.day)

    def get_context_data(self, **kwargs):
        context = super(HistoryView, self).get_context_data(**kwargs)
        context.update({
            'today': self.today,
            'today_calls': self.today_calls,
            'yesterday': self.yesterday,
            'yesterday_calls': self.yesterday_calls
        })
        return context
