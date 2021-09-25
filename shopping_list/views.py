from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .context_processors import available_lists
from .models import List, Item
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_user(request):
    page = 'login'
    context = available_lists(request) | {'page': page}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
    return render(request, 'shopping_list/login_register.html', context)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user = authenticate(request, username=user.username, password=request.POST['password1'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    context = available_lists(request) | {'form': form} | {'page': page}
    return render(request, 'shopping_list/login_register.html', context)


def index(request):
    context = available_lists(request)
    return render(request, 'shopping_list/index.html', context)


def home(request):
    context = available_lists(request)
    return render(request, 'shopping_list/home.html', context)


@login_required(login_url='/login/')
def create_list(request):
    user = request.user
    if request.method == 'POST':
        if request.POST.get("create_list"):
            list_name = request.POST.get("list_name")
            list_budget = request.POST.get("budget")
            new_list, created = List.objects.get_or_create(user=user, name=list_name, budget=list_budget)
            new_list.save()
            print(request.user)
            return HttpResponseRedirect('/list_details/%i' % new_list.id)
    return render(request, 'shopping_list/create_list.html', {})


@login_required(login_url='/login/')
def list_details(request, list_id):
    current_list = get_object_or_404(List, id=list_id)
    if request.method == 'POST':
        if current_list in request.user.shoppinglist.all():
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
            if request.POST.get("edit_item"):
                item_id = request.POST.get("edit_item")
                if request.POST.get("new_item_name"):
                    new_item_name = request.POST.get("new_item_name")
                    current_list.items.filter(pk=item_id).update(name=new_item_name)
                if request.POST.get("new_item_price"):
                    new_item_price = request.POST.get("new_item_price")
                    current_list.items.filter(pk=item_id).update(price=new_item_price)
                current_list.save()
                return HttpResponseRedirect('/list_details/%i' % list_id)
        else:
            return HttpResponse("YOU DON'T HAVE PERMISSION TO EDIT THIS LIST!")
    elif current_list in request.user.shoppinglist.all():
        context = {'list0': current_list} | available_lists(request)
        return render(request, 'shopping_list/detail.html', context)
    else:
        return HttpResponse("YOU DON'T HAVE ACCESS TO THIS PAGE!")
