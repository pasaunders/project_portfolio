"""Views for displaying my different programming projects."""

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request):
    """Home page view."""
    context = {'example': 'example_context'}
    return render(request, 'display_projects/home.html', context=context)
