from rest_framework import serializers
from bites.models import Bite


class BiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bite
        fields = '__all__'
