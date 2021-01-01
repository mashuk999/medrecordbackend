from rest_framework import serializers
from .models import medicines

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = medicines
        fields = '__all__'