from django.urls import path
from . import views

# from teas.views import TeaList

urlpatterns = [
    # ===== MAIN =====
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("teas/", views.teas_index, name="teas_index"),
    path('accounts/signup/', views.signup, name='signup'),
    path("timer/", views.timer, name='timer'),
    # ===== TEAS =====
    path("teas/<int:tea_id>/", views.teas_detail, name="teas_detail"),
    path("teas/create/", views.TeaCreate.as_view(), name="teas_create"),
    path("teas/<int:pk>/update/", views.TeaUpdate.as_view(), name="teas_update"),
    path("teas/<int:pk>/delete/", views.TeaDelete.as_view(), name="teas_delete"),
    path("teas/<int:tea_id>/brew/", views.teas_brew, name="teas_brew"),
    path("teas/<int:tea_id>/restock/", views.teas_restock, name="teas_restock"),
    # ===== COFFEES =====
    path("coffees/", views.coffees_index, name="coffees_index"),
    path("coffees/<int:coffee_id>/", views.coffees_detail, name="coffees_detail"),
    path("coffees/create/", views.CoffeeCreate.as_view(), name="coffees_create"),
    path("coffees/<int:pk>/update/", views.CoffeeUpdate.as_view(), name="coffees_update"),
    path("coffees/<int:pk>/delete/", views.CoffeeDelete.as_view(), name="coffees_delete"),
    path("coffees/<int:coffee_id>/brew/", views.coffees_brew, name="coffees_brew"),
    path("coffees/<int:coffee_id>/restock/", views.coffees_restock, name="coffees_restock"),
]