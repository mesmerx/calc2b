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
def gnuplotlimit(request):
    return render(request, 'polls/gnuplotlimit.html')
def gnuplotdoiseixos(request):
    return render(request, 'polls/gnuplotdoiseixos.html')
def gnuplottreseixos(request):
    return render(request, 'polls/gnuplottreseixos.html')
def gnuplotmulti(request):
    return render(request, 'polls/gnuplotmultiplot.html')
def gnuplotparametrica(request):
    return render(request, 'polls/gnuplotparametrica.html')
def gnuplotcondicionais(request):
    return render(request, 'polls/gnuplotcondicionais.html')
def gnuplotrepeticoes(request):
    return render(request, 'polls/gnuplotrepeticoes.html')
def gnuplotmacros(request):
    return render(request, 'polls/gnuplotmacros.html')
def gnuplotarquivos(request):
    return render(request, 'polls/gnuplotarquivos.html')
