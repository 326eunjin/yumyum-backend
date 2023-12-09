from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'password']
        extra_kwargs = {"password": {"write_only":True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user