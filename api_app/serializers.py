from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UserProfile
        fields = ('id','full_name','bio','phone','address','profile_picture')