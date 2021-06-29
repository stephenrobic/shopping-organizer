from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404 ,render
from .models import List


def index(request):
    latest_lists = List.objects.order_by('-created_on')[:3]
    context = {'latest_lists': latest_lists}
    return render(request, 'shopping_list/index.html', context)


def detail(request, list_id):
    # try:
    #     list0 = List.objects.get(pk=list_id)
    # except List.DoesNotExist:
    #     raise Http404("List does not exist")
    list0 = get_object_or_404(List, pk=list_id)
    return render(request, 'shopping_list/detail.html', {'list0': list0})
    # return HttpResponse("You're looking at list %s." % list_id)
