from rest_framework import serializers

from groups.models import Group
from characteristics.models import Characteristic

class AnimalSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField(max_length=15)

    group = Group(many=True)
    characteristics = Characteristic(many=True)

    

    