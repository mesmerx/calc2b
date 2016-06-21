from django.conf.urls import url

from . import views

urlpatterns = [
 # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^gnuplot$', views.gnuplot, name='gnuplot'),
    url(r'^gnuplot/windows$', views.gnuplotw, name='gnuplotw'),
    url(r'^gnuplot/linux$', views.gnuplotl, name='gnuplotl'),
    url(r'^gnuplot/osx$', views.gnuploto, name='gnuploto'),
    url(r'^gnuplot/basicor2$', views.gnuplotb21, name='gnuplotb21'),
    url(r'^gnuplot/basicor3$', views.gnuplotb31, name='gnuplotb31'),
    url(r'^gnuplot/avançado1$', views.gnuplota1, name='gnuplota1'),
    url(r'^gnuplot/avançado2$', views.gnuplota2, name='gnuplota2'),
    url(r'^gnuplot/avançado3$', views.gnuplota3, name='gnuplota3'),
    url(r'^gnuplot/avançado4$', views.gnuplota4, name='gnuplota4'),
]

