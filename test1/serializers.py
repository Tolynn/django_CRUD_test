from rest_framework import serializers

from test1.models import TestDB


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestDB
        fields = '__all__'
