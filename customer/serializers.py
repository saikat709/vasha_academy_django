# from .models import Profile
from rest_framework import serializers
from customer.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'fullname', 'number', 'password', 'is_verified']  # username is mobile num
        extra_kwargs = {'password': {'write_only': True}, 'id': {'read_only':True} }


    # def create(self, validated_data):
    #     validated_data.pop('confirm_password')  # Remove confirm_password as it's not needed for creation
    #     user = User(
    #         username=validated_data['username'],
    #         email=validated_data['email'],
    #         first_name=validated_data['first_name'],
    #         last_name=validated_data['last_name'],
    #     )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user