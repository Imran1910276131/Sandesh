from rest_framework import serializers
from .models import Profile
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User=get_user_model()
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        Profile.objects.create(user=user)
        return user
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)

        if 'password' in validated_data:
            instance.set_password(validated_data['password'])

        instance.save()
        return instance

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Profile
        fields="__all__"
        read_only_fields=['user']
    
    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['user']=UserSerializer(instance.user).data
        return response

# class WorldSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=World
#         fields="__all__"

# class SportsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Sports
#         fields="__all__"


# class TradeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Trade
#         fields="__all__"




