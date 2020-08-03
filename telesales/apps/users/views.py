from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import (SignUpSerializer, LoginSerializer)
from .renderers import UserRenderer

# Create your views here.


class SignUpView(APIView):
    serializer_class = SignUpSerializer
    renderer_classes = (UserRenderer,)

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    serializer_class = LoginSerializer
    renderer_classes = (UserRenderer,)

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
