from django.urls import path
from . import views

urlpatterns = [
    path("city/", views.Cities.as_view(), name="cities"),
    path("city/<int:city_id>/", views.CityView.as_view(), name="city"),
    path("city/<int:city_id>/street/", views.Streets.as_view(), name="streets"),
    path("shop/", views.Shops.as_view(), name="shops"),
]
