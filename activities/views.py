import json as simplejson
from django.http import HttpResponse

from django.shortcuts import render
from django.views import generic

from django.views.generic import (
    DetailView,
    CreateView,
)

from django.urls import reverse_lazy
from activities.factory import create

from calls.models import (
    Call,
    Contact,
    Tag,
)
from .forms import ContactForm, CallSchedulingForm

import datetime


class PopulateView(generic.View):
    """
    Populates de database
    """
    def get(self, request, *args, **kwargs):
        return create()


class SystemMetricsView(generic.TemplateView):
    """
    View to render the system metrics
    """
    template_name = "system-metrics.html"


class GetTotalCallsView(generic.View):
    """
    Returns info about the calls in JSON format
    """
    def get(self, request, *args, **kwargs):
        wish = request.GET.get('filterby')
        if(wish == 'yearly'):
            return HttpResponse(self.yearly())
        if(wish == 'monthly'):
            return HttpResponse(self.monthly())
        if(wish == 'daily'):
            return HttpResponse(self.daily())

    def yearly(self, *args, **kwargs):
        """
        Returns the calls grouped by year
        """
        json_response = []
        this_year = datetime.datetime.now().year
        for year in range(this_year, this_year-10, -1):
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
        """
        Returns the calls grouped by month
        """
        json_response = []
        this_year = datetime.datetime.now().year
        this_month = datetime.datetime.now().month
        count = 0
        month = this_month
        year = this_year
        while(count != 13):
            month_object = {}
            if(month == 0):
                month = 12
                year -= 1
            elif(month >= 0):
                month_object['month'] = month
                month_object['year'] = year
                month_calls = Call.objects.filter(date__year=year, date__month=month)
                month_object['calls'] = month_calls.count()
                month_object['received'] = month_calls.filter(status='RECEBIDA').count()
                month_object['answered'] = month_calls.filter(status='ATENDIDA').count()
                month_object['declined'] = month_calls.filter(status='ABANDONADA').count()
                month_object['not_answered'] = month_calls.filter(status='NAO_ATENDIDA').count()
                json_response.append(month_object)
                month -= 1
            count += 1
        return simplejson.dumps(json_response)

    def daily(self, *args, **kwargs):
        """
        Returns the calls grouped by day
        """
        today = datetime.datetime.now()
        days_ago = today - datetime.timedelta(days=31)
        days_and_months = []
        end_loop_date = today + datetime.timedelta(days=1)

        while(days_ago.day != end_loop_date.day or
              days_ago.month != end_loop_date.month):

            days_and_months.append({
                'day': days_ago.day,
                'month': days_ago.month,
                'year': days_ago.year
            })
            days_ago = days_ago + datetime.timedelta(days=1)
        json_response = []

        for search_date in days_and_months:
            day_object={}
            day_object['date'] = search_date

            day_calls = Call.objects.filter(
                date__year=search_date['year'],
                date__month=search_date['month'],
                date__day=search_date['day']
            )

            day_object['calls'] = day_calls.count()
            day_object['received'] = day_calls.filter(status='RECEBIDA').count()
            day_object['answered'] = day_calls.filter(status='ATENDIDA').count()
            day_object['declined'] = day_calls.filter(status='ABANDONADA').count()
            day_object['not_answered'] = day_calls.filter(status='NAO_ATENDIDA').count()
            json_response.append(day_object)
        return simplejson.dumps(json_response)


class ScheduleView(generic.ListView):
    model = Call
    template_name = "call-history.html"
    context_object_name = 'calls'
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
        context = super(ScheduleView, self).get_context_data(**kwargs)
        context.update({
            'today': self.today,
            'today_calls': self.today_calls,
            'yesterday': self.yesterday,
            'yesterday_calls': self.yesterday_calls
        })
        return context


class HistoryActivitiesView(generic.ListView):
    """
    View to access the history of acitivities
    """
    template_name = "history-agenda.html"
    model = Call


class ClientsView(CreateView):
    """
    View to handles the clients
    """
    model = Contact
    template_name = 'clients.html'
    form_class = ContactForm
    success_url = reverse_lazy('activities:clients')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, *kwargs)
        context["tags"] = Tag.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        raw_tags = form.cleaned_data['raw_tags'].split(',')

        for raw_tag in raw_tags:
            tag = Tag.objects.filter(name=raw_tag)
            form.instance.tag.add(tag.get(name=raw_tag))

        return super(ClientsView, self).form_valid(form)

    def form_invalid(self, form):
        return super(ClientsView, self).form_invalid(form)
        # import ipdb
        # ipdb.set_trace()

class CallSchedulingRegisterView(CreateView):
    model = Call
    template_name = 'call-scheduling.html'
    form_class = CallSchedulingForm
    success_url = reverse_lazy('activities:call-scheduling')

    def form_valid(self, form):
        # import ipdb
        # ipdb.set_trace()
        return super(CallSchedulingRegisterView, self).form_valid(form)

    def form_invalid(self, form):
        # import ipdb
        # ipdb.set_trace()
        return super(CallSchedulingRegisterView, self).form_invalid(form)
