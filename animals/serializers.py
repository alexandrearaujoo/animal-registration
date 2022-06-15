from unicodedata import name
from rest_framework import serializers

from characteristics.models import Characteristic
from groups.models import Group
from animals.models import Animal

from groups.serializers import GroupSerializer
from characteristics.serializers import CharacteristicSerializer

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField(max_length=15)

    group = GroupSerializer()
    characteristics = CharacteristicSerializer(many=True)

    def create(self, validated_data):
        group = validated_data.pop('group')
        characteristics = validated_data.pop('characteristics')

        group, _ = Group.objects.get_or_create(**group)
        animal = Animal.objects.create(**validated_data, group=group)

        for characteristic in characteristics:
            c, _ = Characteristic.objects.get_or_create(**characteristic)
            animal.characteristics.add(c)

        return animal

    def update(self, instance, validated_data):
        keys_not_available = ('sex', 'group',)

        for key, value in validated_data.items():
            if key in keys_not_available:
                raise KeyError(key)

            if key == "characteristics" and type(value) == list:
                for characteristic in value:
                    c, _ = Characteristic.objects.get_or_create(**characteristic)
                    instance.characteristics.add(c)
            
            else:
                setattr(instance, key, value)

        instance.save()

        return instance
