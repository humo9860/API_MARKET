from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


from .serializers import UserSeril
from .models import User

class UserCreateListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSeril
    
    
class UserDetailview(RetrieveUpdateDestroyAPIView):
    queryset = User .objects.all()
    serializer_class = UserSeril
    lookup_field = 'id'

# Create your views here.
