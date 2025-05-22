from rest_framework import serializers
from .models import LostFoundID

class LostFoundIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostFoundID
        fields = '__all__'
        read_only_fields = ('user', 'date_reported')
