"""Frontend Views."""
from django.shortcuts import render


def index(request):
    """Index View."""
    return render(request, "frontend/index.html")
