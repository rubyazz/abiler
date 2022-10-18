import calendar

from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import context
from django.urls import reverse
from django.views import View
from .utils import Calendar
from datetime import datetime, date, timedelta
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe

from .forms import UserRegisterForm, UserLoginForm, EventForm
from .models import *

#
# def index(request):
#     return render(request, "index.html")


def abi(request):
    a = Abies.objects.all()
    context = {'a': a}
    return render(request, "abiler.html", context)


def help(request):
    return render(request, "help.html")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, ' Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {"form":form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect( 'calendar')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {"form":form})


def user_logout(request):
    logout(request)
    return redirect('login')


class MyView(LoginRequiredMixin, View):
    login_url = '/program/'
    redirect_field_name = 'redirect_to'


# def index(request):
#     return HttpResponse('hello')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'event.html', {'form': form})