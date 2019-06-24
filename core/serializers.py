# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        # fields you want to expose
        fields = ('id', 'name', 'address', 'professions', 'data_sheet')


 