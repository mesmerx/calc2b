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
def gnuplotl(request):
    return render(request, 'polls/gnuplotlinux.html')
def gnuploto(request):
    return render(request, 'polls/gnuplotosx.html')
def gnuplotb21(request):
    return render(request, 'polls/gnuplotb21.html')

