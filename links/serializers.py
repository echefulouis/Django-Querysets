from rest_framework import serializers
from .models import Link

class LinkSerializer(serializers.ModelSerializer):
    class meta:
        meta = Link
        fields="__all__"