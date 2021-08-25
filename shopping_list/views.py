from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .context_processors import available_lists
from .models import List, Item


def index(request):
    context = available_lists(request)
    return render(request, 'shopping_list/index.html', context)


def home(request):
    context = available_lists(request)
    return render(request, "shopping_list/home.html", context)


def create_list(request):
    context = available_lists(request)
    if request.method == 'POST':
        if request.POST.get("create_list"):
            list_name = request.POST.get("list_name")
            list_budget = request.POST.get("budget")
            new_list = List(name=list_name, budget=list_budget)
            new_list.save()
            print(request.user)
            return HttpResponseRedirect('/list_details/%i' % new_list.id)
    return render(request, 'shopping_list/create_list.html', context)


def list_details(request, list_id):
    if request.method == 'POST':
        current_list = get_object_or_404(List, id=list_id)
        if request.POST.get("add_item"):
            item_name = request.POST.get("item_name")
            item_price = request.POST.get("item_price")
            item = Item(name=item_name, price=item_price)
            item.save()
            current_list.items.add(item)
            print(request.user)
            return HttpResponseRedirect('/list_details/%i' % list_id)
        if request.POST.get("remove_item"):
            item_id_list = request.POST.getlist("item")
            for item_id in item_id_list:
                current_item = get_object_or_404(Item, pk=item_id)
                current_list.items.remove(current_item)
            return HttpResponseRedirect('/list_details/%i' % list_id)
        if request.POST.get("remove_list"):
            current_list.delete()
            return HttpResponseRedirect('/')
        if request.POST.get("edit_list"):
            if request.POST.get("new_list_name"):
                new_list_name = request.POST.get("new_list_name")
                current_list.name = new_list_name
            if request.POST.get("new_list_budget"):
                new_list_budget = request.POST.get("new_list_budget")
                current_list.budget = new_list_budget
            current_list.save()
            return HttpResponseRedirect('/list_details/%i' % list_id)
    list0 = get_object_or_404(List, pk=list_id)
    context = {'list0': list0} | available_lists(request)
    return render(request, 'shopping_list/detail.html', context)
