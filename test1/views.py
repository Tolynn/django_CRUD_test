from django.shortcuts import render

from rest_framework import viewsets

from test1.models import TestDB
from test1.serializers import TestSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = TestDB.objects.all()
    serializer_class = TestSerializer
