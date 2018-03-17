from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
    
    # https://stackoverflow.com/a/38382056
    def create(self, validated_data):
        user = models.User.objects.create(**validated_data)

        user.set_password(validated_data['password'])
        user.save()
        
        return user

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = '__all__'

class SpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Space
        fields = '__all__'

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Storage
        fields = '__all__'