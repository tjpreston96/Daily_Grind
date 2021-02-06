from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tea, Coffee

# ============ HOME & INDEX ============
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


# ============ TEAS ============
def teas_index(request):
    teas = Tea.objects.all()
    return render(request, "teas/index.html", {"teas": teas})


def teas_detail(request, tea_id):
    tea = Tea.objects.get(id=tea_id)
    return render(request, "teas/detail.html", {"tea": tea})


class TeaCreate(CreateView):
    model = Tea
    fields = "__all__"


class TeaUpdate(UpdateView):
    model = Tea
    fields = "__all__"


class TeaDelete(DeleteView):
    model = Tea
    success_url = "/teas/"


# ============ COFFEES ============
def coffees_index(request):
    coffees = Coffee.objects.all()
    return render(request, "coffees/index.html", {"coffees": coffees})


def coffees_detail(request, coffee_id):
    coffee = Coffee.objects.get(id=coffee_id)
    return render(request, "coffees/detail.html", {"coffee": coffee})


class CoffeeCreate(CreateView):
    model = Coffee
    fields = "__all__"


class CoffeeUpdate(UpdateView):
    model = Coffee
    fields = "__all__"


class CoffeeDelete(DeleteView):
    model = Coffee
    success_url = "/coffees/"