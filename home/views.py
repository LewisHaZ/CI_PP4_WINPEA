# Imports
# 3rd Party
from django.shortcuts import render

# Internal


def home(request):
    """
    Display home page
    """
    return render(request, 'home/index.html')
