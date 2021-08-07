from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404 ,render, redirect
from .models import List, Item


def index(request):
    latest_lists = List.objects.order_by('-created_on')[:3]
    context = {'latest_lists': latest_lists}
    return render(request, 'shopping_list/index.html', context)


def home(request):
    return render(request, "shopping_list/home.html", {})


def create_list(request):
    if request.method == 'POST':
        if request.POST.get("create_list"):
            list_name = request.POST.get("list_name")
            list_budget = request.POST.get("budget")
            new_list = List(name=list_name, budget=list_budget)
            new_list.save()
            print(request.user)
            return HttpResponseRedirect('/list_details/%i' % new_list.id)
    return render(request, 'shopping_list/create_list.html', {})


def list_details(request, list_id):
    if request.method == 'POST':
        if request.POST.get("add_item"):
            current_list = get_object_or_404(List, id=list_id)
            item_name = request.POST.get("item_name")
            item_price = request.POST.get("item_price")
            item = Item(name=item_name, price=item_price)
            item.save()
            current_list.items.add(item)
            print(request.user)
            return HttpResponseRedirect('/list_details/%i' % current_list.id)
    list0 = get_object_or_404(List, pk=list_id)
    return render(request, 'shopping_list/detail.html', {'list0': list0})
