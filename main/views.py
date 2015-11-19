from django.shortcuts import render, render_to_response

from django.template import RequestContext

from main.models import DvdList, DvdCas
from django.http import JsonResponse

from django.core.paginator import Paginator, InvalidPage, EmptyPage

# from django.views.generic.list import ListView

# Create your views here.


def dvd_list(request):

    api_dict = {}

    dvds = Dvd.objects.filter(title__istartswith=letter)   

    page = int(request.GET.get("page", '1'))

    letter = request.GET.get('letter', 'A')

    print page 

    paginator = Paginator(dvds, 20)

    try:
        dvds = paginator.page(page)
    except (InvalidPage, EmptyPage):
        dvds = paginator.page(paginator.num_pages)    

    dvd_list = []

    for dvd in dvds:
        dvd_list.append({'title': dvd.title,
                           'studio': dvd.studio.studio,
                           'price': dvd.price,
                           'rating': dvd.rating,
                           'genre': dvd.genre.genre,
                           'pk': dvd.pk,
                           })

    api_dict['dvds'] = dvd_list

    try:
        api_dict['next_page'] = dvds.next_page_number()
    except:
        pass

    try:
        api_dict['previous_page'] = dvds.previous_page_number()
    except:
        pass

    api_dict['current_page'] = dvds.number

    api_dict['all_pages'] = dvds.paginator.num_pages

    api_dict['letters'] = list(string.ascii_uppercase)

    return JsonResponse(api_dict)


def dvd_list_dbv(request):

    context = {}

    dvd_list = DvdList.objects.all()[:300]

    context['dvd_list'] = dvd_list

    paginator = Paginator(dvd_list, 20)

    page = int(request.GET.get("page", '1'))

    try:
        dvd_list = paginator.page(page)
    except (InvalidPage, EmptyPage):
        dvd_list = paginator.page(paginator.num_pages)

    context['dvd_list'] = dvd_list

    return render_to_response('dvd_list_dbv.html', context, context_instance=RequestContext(request))


def dvd_list(request):
    dvds = Dvd_List.objects.all()[:300]
    api_dict = {}
    dvd_list = []
    api_dict['dvd_list'] = dvd_list

    api_dict['letters'] = list(string.ascii_uppercase)

    for dvd in dvds:
        dvd_list.append({'dvd_title': dvd.dvd_title,
                            'studio': dvd.studio.studio,
                            'price': dvd.price,
                            'rating': dvd.rating,
                            'genre': dvd.genre.genre,
                            'release': dvd.released,
                            'pk': dvd.pk,
                        })

    return JsonResponse(api_dict)


# class DvdList(ListView):  
#         model = DvdList
#         queryset = DvdList.objects.all()[:300]
#         template_name = "dvd_list_cbv.html"
#         context_object_name = "dvd_title"
#         paginate_by = 20


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