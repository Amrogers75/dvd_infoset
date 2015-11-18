from django.shortcuts import render, render_to_response

from django.template import RequestContext

from main.models import DvdList, DvdCas
from django.http import JsonResponse

# Create your views here.


def dvd_detail(request, pk):

    dvds = Dvd_list.objects.get(pk=pk)

    for dvd in dvds:
        dvd_detail = ({'dvd_title': dvd.dvd_title,
                        'studio': dvd.studio,
                        'price': dvd.price,
                        'rating': dvd.rating,
                        'genre': dvd.genre,
                        'release': dvd.released,
                        })

    return render_to_response('dvdlist.html', context, context_instance=RequestContext(request))


def dvd_list_cas(request):

    context = {}

    dvd_list = DvdCas.objects.all()

    context['dvd_list'] = dvd_list

    return render_to_response('dvdlist.html', context, context_instance=RequestContext(request))


def dvd_list_templ(request):

    context = {}

    dvd_list = Dvd.objects.all()

    context['dvd_list'] = dvd_list

    return render_to_response('dvd_list.html', context, context_instance=RequestContext(request))


def dvd_list_mysql(request):

    context = {}

    dvd_list = Dvd.objects.all()

    context['dvd_list'] = dvd_list

    return render_to_response('dvd_list.html', context, context_instance=RequestContext(request))


def dvd_list(request):
    dvds = Dvd_List.objects.all()[:300]
    api_dict = {}
    dvd_list = []
    api_dict['dvd_list'] = dvd_list

    for dvd in dvds:
        dvd_list.append({'dvd_title': dvd.dvd_title,
                            'studio': dvd.studio,
                            'price': dvd.price,
                            'rating': dvd.rating,
                            'genre': dvd.genre,
                            'release': dvd.released,
                        })
    return JsonResponse(api_dict)


def dvd_detail(request, pk):

    dvds = Dvd_list.objects.get(pk=pk)

    for dvd in dvds:
        dvd_detail = ({'dvd_title': dvd.dvd_title,
                        'studio': dvd.studio,
                        'price': dvd.price,
                        'rating': dvd.rating,
                        'genre': dvd.genre,
                        'release': dvd.released,
                        })

    return JsonResponse(dvd_detail)