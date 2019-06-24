from django.shortcuts import render
from .models import Customer
from rest_framework import viewsets
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all() 
    serializer_class = CustomerSerializer

 