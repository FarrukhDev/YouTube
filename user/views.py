from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from user.models import Account
from user.serializer import UserSerializer
from rest_framework.filters import SearchFilter

class UserListCreateAPIView(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    search_fields = ["name"]

    def get_object(self):
        return self.request.user

class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    search_fields = ["name"]

    def get_object(self):
        return self.request.user
