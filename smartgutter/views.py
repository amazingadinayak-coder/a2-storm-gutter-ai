from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import CityWorkerSignupForm, HomeownerSignupForm
from .models import Gutter


def home(request):
    """Landing page for SmartGutter AI."""
    return render(request, 'smartgutter/home.html')


def problem(request):
    """Problem statement page."""
    return render(request, 'smartgutter/problem.html')


def solution(request):
    """Solution and system design page."""
    return render(request, 'smartgutter/solution.html')


def how_it_works(request):
    """User experience and collaboration page."""
    return render(request, 'smartgutter/how_it_works.html')


def register_page(request):
    """Hub for homeowner and city worker registration."""
    return render(request, 'smartgutter/register.html')


def homeowner_signup(request):
    if request.method == 'POST':
        form = HomeownerSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Thanks—you are signed up. The city may contact you using the details you provided.',
            )
            return redirect('homeowner_signup')
    else:
        form = HomeownerSignupForm()
    return render(
        request,
        'smartgutter/homeowner_signup.html',
        {'form': form},
    )


def city_worker_signup(request):
    if request.method == 'POST':
        form = CityWorkerSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Registration received. Your availability is on file for scheduling.',
            )
            return redirect('city_worker_signup')
    else:
        form = CityWorkerSignupForm()
    return render(
        request,
        'smartgutter/city_worker_signup.html',
        {'form': form},
    )


def gutter_priorities(request):
    gutters = Gutter.objects.filter(needs_cleaning=True)
    return render(
        request,
        'smartgutter/gutter_priorities.html',
        {'gutters': gutters},
    )
