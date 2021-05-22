from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView

from main.models import Search
from main.serializers import SearchSerializer


class SendtoAIView(viewsets.ModelViewSet):
    serializer_class = SearchSerializer
    queryset = Search.objects.all()
