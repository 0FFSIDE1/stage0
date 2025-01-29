from datetime import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class UserData(APIView):
    def get(self, request):
        data = {
            'email': 'offsideint@gmail.com',
            'date': datetime.utcnow().isoformat() + "Z",
            'github_url': ''
        }
        return Response(data, status=status.HTTP_200_OK)