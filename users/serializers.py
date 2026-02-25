from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from users.models import SocialMedia


class CustomUserCreateSerializer(UserCreateSerializer): 
    profile_image = serializers.ImageField(required = False, allow_null = True)
    cover_image = serializers.ImageField(required=False, allow_null=True)
    class Meta(UserCreateSerializer.Meta): 
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'phone_number', 'address', 'profile_image', 'cover_image', 'bio']
        
    
class CustomUserSerializer(UserSerializer):
    profile_image = serializers.ImageField(required=False, allow_null=True)
    cover_image = serializers.ImageField(required=False, allow_null=True)
    class Meta(UserSerializer.Meta): 
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'profile_image', 'cover_image', 'bio']
        ref_name = 'CustomUser'


class SocialMediaSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = SocialMedia
        fields = ['id', 'user', 'site_name', 'icon', 'link']
        read_only_fields = ['user']
