from django.shortcuts import render


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
    """Registration information for city and homeowners."""
    return render(request, 'smartgutter/register.html')
