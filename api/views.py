from django.shortcuts import render
from django.core.exceptions import SuspiciousOperation, FieldError
from django.db.models import Q,F

from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response

from api.models import City, Street, Shop
from api.serializers import CitySerializer, StreetSerializer, ShopSerializer

from datetime import datetime
# Create your views here.

class Cities(APIView):
    def get(self, request, format = None):
        cities = CitySerializer(City.objects.all(), many=True)
        return Response(cities.data)

class CityView(APIView):
    def get(self, request, city_id, format = None):
        try:
            city = City.objects.get(id = city_id)
            return Response(CitySerializer(city).data)
        except Exception as e: 
           raise SuspiciousOperation


class Streets(APIView):
    def get(self, request, city_id, format = None):
        try:
            city = City.objects.get(id = city_id)
            return Response(StreetSerializer(Street.objects.filter(city=city), many=True).data)
        except Exception as e:
           raise SuspiciousOperation

class Shops(APIView):
    def get(self, request, format = None):
        try:
            query = request.query_params
            street = query.get("street", None)
            if street:
                street = Q(street__name=street)
            else:
                street = Q()
            city = query.get("city", None)
            if city:
                city = Q(city__name=city)

            else:
                city = Q()
            open = query.get("open", None)
            if open=="1":
                open = Q(opening_hour__gte=F("closing_hour"))&Q(Q(opening_hour__lte=datetime.now().time())|Q(closing_hour__gte=datetime.now().time()))|Q(opening_hour__lte=F("closing_hour"))&Q(Q(opening_hour__lte=datetime.now().time())&Q(closing_hour__gte=datetime.now().time()))
            elif open =="0":
                 open = Q(opening_hour__gte=F("closing_hour"))&~Q(Q(opening_hour__lte=datetime.now().time())|Q(closing_hour__gte=datetime.now().time()))|Q(opening_hour__lte=F("closing_hour"))&~Q(Q(opening_hour__lte=datetime.now().time())&Q(closing_hour__gte=datetime.now().time()))
            else:
                open = Q()
            shops = Shop.objects.filter(street&city&open)
            return Response(ShopSerializer(shops, many=True).data)
        except Exception as e:
            raise SuspicuiousOperation
    def post(self, request):
        try:
            s =Shop.objects.create(**request.data)
            s.save()
            return Response(ShopSerializer(s).data)
        except Exception as e:
            raise SuspicuiousOperation
