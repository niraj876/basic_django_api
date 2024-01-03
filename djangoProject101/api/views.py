from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
# create basic get and post api for testing purpose


class DemoApi(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})

    def post(self, request):
        return Response({"message": "Got some data!", "data": request.data})