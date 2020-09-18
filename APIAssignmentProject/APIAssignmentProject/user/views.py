from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import UserSerializer
from .models import User
from rest_framework import status
from rest_framework import serializers

from rest_framework.response import Response
# Create your views here.


class LoginOrRegister(APIView):

    serializer_class = UserSerializer

    def post(self, request, format=None):

        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if (username and email and password):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                Response_data = {
                    "data": serializer.data,
                    "msg": "Register successfully"
                }
                return Response(Response_data)
            else:
                return Response(serializer.errors)
        elif (username and password):
            user = User.objects.filter(
                username=username, password=password).first()
            if user:
                serializer = UserSerializer(user)
                Response_data = {
                    "data": serializer.data,
                    "msg": "Login successfully"
                }
                return Response(Response_data, status=status.HTTP_200_OK)
            else:
                return Response({"msg": "User credential failed"}, status=status.HTTP_400_BAD_REQUEST)
