from .models import Cuenta
from rest_framework import serializers

class SaldoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = "__all__"