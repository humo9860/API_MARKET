from rest_framework import serializers

from .models import User


class UserSeril(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'photo']
        extra_kwargs = {'password':{'write_only':True}}
        

def create(self, validated_data):
    password = validated_data.pop('password')
    user = User.objects.create(**validated_data)
    user.set_password('password')
    user.save()
    return user