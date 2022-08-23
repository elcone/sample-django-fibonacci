from rest_framework import serializers

from .fibonacci import fibonacci
from .models import NumberRequested


class NumberRequestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberRequested
        fields = '__all__'

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.result = fibonacci(instance.number)
        instance.save()

        return instance
