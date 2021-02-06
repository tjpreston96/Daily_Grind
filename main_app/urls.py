from django.urls import path
from . import views

# from teas.views import TeaList

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("teas/", views.teas_index, name="teas_index"),
    path("teas/<int:tea_id>/", views.teas_detail, name="teas_detail"),
    path("teas/create/", views.TeaCreate.as_view(), name="teas_create"),
    path("teas/<int:pk>/update/", views.TeaUpdate.as_view(), name="teas_update"),
    path("teas/<int:pk>/delete/", views.TeaDelete.as_view(), name="teas_delete"),
    path("coffees/", views.coffees_index, name='coffees_index'),
    path("coffees/<int:coffee_id>/", views.coffees_detail, name='coffees_detail')
]