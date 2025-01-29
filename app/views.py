from datetime import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

class UserData(APIView):
    """
    API endpoint to retrieve user data including email, current datetime, and GitHub URL.
    """

    @swagger_auto_schema(
        operation_description="Retrieve user data including email, current datetime, and GitHub URL.",
        responses={
            200: openapi.Response(
                description="User data retrieved successfully",
                examples={
                    "application/json": {
                        "email": "offsideint@gmail.com",
                        "current_datetime": "2025-01-29T12:34:56.789123Z",
                        "github_url": "https://github.com/0FFSIDE1/stage0"
                    }
                },
            )
        },
    )
    def get(self, request):
        """
        Retrieve user data including:
        - Email
        - Current datetime (ISO format)
        - GitHub repo URL
        """
        data = {
            'email': 'offsideint@gmail.com',
            'current_datetime': datetime.utcnow().isoformat() + "Z",
            'github_url': 'https://github.com/0FFSIDE1/stage0'
        }
        return Response(data, status=status.HTTP_200_OK)
    
# (datetime.utcnow() + timedelta(hours=1)).isoformat() + "Z"