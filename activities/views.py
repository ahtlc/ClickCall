import json as simplejson
from django.http import HttpResponse

from django.shortcuts import render
from django.views import generic
from calls.models import Call
from activities.objects import Year
import datetime

class TestView(generic.TemplateView):
    template_name = "call-history.html"

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
            json_response.append(year_object)
        return simplejson.dumps(json_response)
    def monthly(self, *args, **kwargs):
        json_response = []
        this_year = datetime.datetime.now().year
        this_month = datetime.datetime.now().month
        count = 0
        month = this_month
        year = this_year
        while(count!=13):
            month_object = {}
            if(month == 0):
                month = 12
                year-=1
            elif(month>=0):
                month_object['month'] = month
                month_object['year'] = year
                month_object['calls'] = Call.objects.filter(date__year=year, date__month=month).count()
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
            day_object['calls'] = Call.objects.filter(date__year=search_date['year'], date__month=search_date['month'],date__day=search_date['day']).count()
            json_response.append(day_object)
        return simplejson.dumps(json_response)
