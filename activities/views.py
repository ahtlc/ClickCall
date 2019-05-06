import json as simplejson
from django.http import HttpResponse

from django.shortcuts import render
from django.views import generic
from calls.models import Call
from activities.objects import Year

from calls.models import Contact
from .forms import ContactForm
from django.views. generic import CreateView
from django.urls import reverse_lazy

import datetime


class ClientsView(generic.TemplateView):
    template_name = "clients.html"


class GetTotalCallsView(generic.View):
    def get(self, request, *args, **kwargs):
        wish = request.GET.get('filterby')
        if(wish == 'yearly'):
            return HttpResponse(self.yearly())
        if(wish == 'monthly'):
            return HttpResponse(self.monthly())
        if(wish == 'daily'):
            return HttpResponse(self.daily())
    def yearly(self, *args, **kwargs):
        json_response = []
        this_year = datetime.datetime.now().year
        for year in range(this_year, this_year-10,-1):
            year_object = {}
            this_year_calls = Call.objects.filter(date__year=year)
            number_of_calls = this_year_calls.count()
            year_object['year'] = year
            year_object['calls'] = number_of_calls
            year_object['received'] = this_year_calls.filter(status='RECEBIDA').count()
            year_object['answered'] = this_year_calls.filter(status='ATENDIDA').count()
            year_object['declined'] = this_year_calls.filter(status='ABANDONADA').count()
            year_object['not_answered'] = this_year_calls.filter(status='NAO_ATENDIDA').count()
            json_response.append(year_object)
        return simplejson.dumps(json_response)
    def monthly(self, *args, **kwargs):
        json_response = []
        this_year = datetime.datetime.now().year
        this_month = datetime.datetime.now().month
        count = 0
        month = this_month
        year = this_year
        import ipdb; ipdb.set_trace()
        while(count!=13):
            month_object = {}
            if(month == 0):
                month = 12
                year-=1
            elif(month>=0):
                month_object['month'] = month
                month_object['year'] = year
                month_calls = Call.objects.filter(date__year=year, date__month=month)
                month_object['calls'] = month_calls.count()
                month_object['received'] = month_calls.filter(status='RECEBIDA').count()
                month_object['answered'] = month_calls.filter(status='ATENDIDA').count()
                month_object['declined'] = month_calls.filter(status='ABANDONADA').count()
                month_object['not_answered'] = month_calls.filter(status='NAO_ATENDIDA').count()
                json_response.append(month_object)
                month-=1
            count+=1
        return simplejson.dumps(json_response)
    def daily(self, *args, **kwargs):
        today = datetime.datetime.now()
        days_ago = today - datetime.timedelta(days=31)
        days_and_months = []
        end_loop_date = today + datetime.timedelta(days=1)
        while(days_ago.day != end_loop_date.day or days_ago.month!=end_loop_date.month):
            days_and_months.append({
                'day': days_ago.day,
                'month':days_ago.month,
                'year': days_ago.year
            })
            days_ago = days_ago + datetime.timedelta(days=1)
        json_response = []
        for search_date in days_and_months:
            day_object={}
            day_object['date'] = search_date
            day_calls = Call.objects.filter(date__year=search_date['year'], date__month=search_date['month'],date__day=search_date['day'])
            day_object['calls'] = day_calls.count()
            day_object['received'] = day_calls.filter(status='RECEBIDA').count()
            day_object['answered'] = day_calls.filter(status='ATENDIDA').count()
            day_object['declined'] = day_calls.filter(status='ABANDONADA').count()
            day_object['not_answered'] = day_calls.filter(status='NAO_ATENDIDA').count()
            json_response.append(day_object)
        return simplejson.dumps(json_response)


class HistoryActivitiesView(generic.ListView):
    template_name = "history-agenda.html"
    model = Call
    context_object_name = 'call'
    queryset = Call.objects.all()

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)

    today_calls = Call.objects.filter(
            date__year=today.year,
            date__month=today.month,
            date__day=today.day
    )

    yesterday_calls = Call.objects.filter(
            date__year=yesterday.year,
            date__month=yesterday.month,
            date__day=yesterday.day
    )

    def get_context_data(self, **kwargs):
        context = super(HistoryActivitiesView, self).get_context_data(**kwargs)
        context.update({
            'today': self.today,
            'today_calls': self.today_calls,
            'yesterday': self.yesterday,
            'yesterday_calls': self.yesterday_calls
        })
        return context

class ContactRegisterView(CreateView):
    model = Contact
    template_name = 'new_contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('activities:contact_new')

    def form_valid(self, form):
        # import ipdb
        # ipdb.set_trace()
        return super(ContactRegisterView, self).form_valid(form)

    def form_invalid(self,form):
        # import ipdb
        # ipdb.set_trace()
        return super(ContactRegisterView, self).form_invalid(form)
