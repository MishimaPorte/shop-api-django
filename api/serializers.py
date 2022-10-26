from rest_framework.serializers import ModelSerializer, SlugRelatedField
from api.models import City, Street, Shop

class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ["id", "name"]

class StreetSerializer(ModelSerializer):

    city = SlugRelatedField(
        read_only=True,
        slug_field="name"
    )
    class Meta:
        fields = ["id", "name", "city"]
        model = Street

class ShopSerializer(ModelSerializer):
    city = SlugRelatedField(
        read_only=True,
        slug_field="name"
    )
    
    street = SlugRelatedField(
        read_only=True,
        slug_field="name"
    )
    class Meta:
        fields = ["id", "name", "city", "street", "address", "opening_hour", "closing_hour"]
        model = Shop
