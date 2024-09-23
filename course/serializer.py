from .models import Coursetype,Attendcourse
from rest_framework import serializers

class Coursetypeserializer(serializers.ModelSerializer):
    class Meta:
        model=Coursetype
        fields='__all__'


class Attendserializer(serializers.ModelSerializer):
    class Meta:
        model=Attendcourse
        fields="__all__"