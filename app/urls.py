from django.urls import path
from .views import UserData
urlpatterns = [
    
    path('data', UserData.as_view(), name='data'),
]