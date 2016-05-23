from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render

from .models import Paginas

from django.http import Http404
    
def index(request):
    return render(request, 'polls/inicio.html')
    
def gnuplot(request):
    return render(request, 'polls/gnuplot.html')
def gnuplotw(request):
    return render(request, 'polls/gnuplotwindows.html')

