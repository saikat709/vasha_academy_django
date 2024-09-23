from .models import Question,UserAnswer
from rest_framework import serializers

class Questionserializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields="__all__"
        extra_kwargs = {'ans': {'write_only': True}}



class Useranswerserializer(serializers.ModelSerializer):
    class Meta:
        model=UserAnswer
        fields="__all__"
        


