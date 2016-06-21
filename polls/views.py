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
def gnuplotb31(request):
    return render(request, 'polls/gnuplotb31.html')
def gnuplota1(request):
    return render(request, 'polls/gnuplota1.html')
def gnuplota2(request):
    return render(request, 'polls/gnuplota2.html')
def gnuplota3(request):
    return render(request, 'polls/gnuplota3.html')
def gnuplota4(request):
    return render(request, 'polls/gnuplota4.html')

