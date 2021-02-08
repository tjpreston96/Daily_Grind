from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import F
from .models import Tea, Coffee
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# ============ AUTHENTICATION ============
def signup(request):
    error_message = ""
    if request.method == "POST":
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect("home")
        else:
            error_message = "Invalid Sign Up - Try Again"
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)


# ============ HOME & INDEX ============
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def timer(request):
    return render(request, "timer.html")


# ============ TEAS ============
@login_required
def teas_index(request):
    teas = Tea.objects.filter(user=request.user)
    return render(request, "teas/index.html", {"teas": teas})


@login_required
def teas_detail(request, tea_id):
    tea = Tea.objects.get(id=tea_id)
    return render(request, "teas/detail.html", {"tea": tea})


@login_required
def teas_brew(request, tea_id):
    tea = Tea.objects.get(id=tea_id)
    tea.quantity -= 1
    tea.save()
    return redirect("teas_index")


@login_required
def teas_restock(request, tea_id):
    tea = Tea.objects.get(id=tea_id)
    tea.quantity += tea.quantPerBox
    tea.save()
    return redirect("teas_index")


class TeaCreate(LoginRequiredMixin, CreateView):
    model = Tea
    fields = ["name", "variety", "description", "strength", "quantity", "quantPerBox"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TeaUpdate(LoginRequiredMixin, UpdateView):
    model = Tea
    fields = "__all__"


class TeaDelete(LoginRequiredMixin, DeleteView):
    model = Tea
    success_url = "/teas/"


# ============ COFFEES ============
@login_required
def coffees_index(request):
    coffees = Coffee.objects.filter(user=request.user)
    return render(request, "coffees/index.html", {"coffees": coffees})


@login_required
def coffees_detail(request, coffee_id):
    coffee = Coffee.objects.get(id=coffee_id)
    return render(request, "coffees/detail.html", {"coffee": coffee})


@login_required
def coffees_brew(request, coffee_id):
    coffee = Coffee.objects.get(id=coffee_id)
    coffee.servings -= 1
    coffee.save()
    return redirect("coffees_index")


@login_required
def coffees_restock(request, coffee_id):
    coffee = Coffee.objects.get(id=coffee_id)
    coffee.servings += coffee.servPerBag
    coffee.save()
    return redirect("coffees_index")


class CoffeeCreate(LoginRequiredMixin, CreateView):
    model = Coffee
    fields = ["name", "variety", "description", "strength", "servings", "servPerBox"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CoffeeUpdate(LoginRequiredMixin, UpdateView):
    model = Coffee
    fields = "__all__"


class CoffeeDelete(LoginRequiredMixin, DeleteView):
    model = Coffee
    success_url = "/coffees/"

