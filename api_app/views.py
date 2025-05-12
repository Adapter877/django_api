from django.shortcuts import render
from django.http import HttpRequest
from .models import UserProfile
from rest_framework import generics,permissions,status
from .serializers import UserProfileSerializer
from rest_framework.response import Response
import requests
import json
from urllib.request import urlopen
# Create your views here.

def index(request):
    response = requests.get('http://localhost:8000/api/job/')
    data = response.json()
    return render(request,'index.html',{'data':data})

class UserProfile_list(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
  #  permission_classes = [permissions.IsAuthenticated]
class UserProfile_DetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
  #  permission_classes = [permissions.IsAuthenticated]

