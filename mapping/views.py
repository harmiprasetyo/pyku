from django.shortcuts import redirect, render
from django.http import Http404
from django.contrib import messages
def map_view(request):
    return render(request, 'map/mapindo.html')