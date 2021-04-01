import json

from rest_framework import generics,filters,viewsets,status
from djongo import models as djmodels
from .models import Ghazals
from .serializers import GhazalsSerializer
from django_filters.rest_framework import DjangoFilterBackend

import os
from django.core import serializers
from rest_framework.response import  Response

from django.conf import settings

class GhazalsViewSet(viewsets.ModelViewSet):
    queryset = Ghazals.objects.all()
    serializer_class = GhazalsSerializer

    def create(self, request, *args, **kwargs):
        baseDir = (settings.FILES_DIR)
        serialized_data =self.serializer_class(data=request.data)
        print(serialized_data.is_valid())
        serialized_data.save()
        return Response(status = status.HTTP_201_CREATED)

    def list(self, request):
        data = Ghazals.objects.filter(author_name="a-g-josh")
        print(data.count())
        serializer = GhazalsSerializer(data=data, many=True)
        return Response(serializer.data)

    def detail(self, request):
        data = Ghazals.objects.all()  #.filter(author_name="a-g-josh")
        print(data)
        serialized_data =self.serializer_class(data=data)
        if serialized_data.is_valid():
            return Response(data= serialized_data.data ,status = status.HTTP_201_CREATED)
        return Response(data = serialized_data.error,status = status.HTTP_400_BAD_REQUEST)


class CommandoViewSet( viewsets.ModelViewSet):
    fields = ('cleaned_content')
    queryset = Ghazals.objects.only( fields)

    # for e in queryset:
    #     print(e._id)
    # serializer_class = GhazalsSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['author_name', 'author_alphabet']

    def get_queryset(self):
        fields = ('cleaned_content')
        print("Reached")
        # grams = self.request.query_params.get('grams')
        # s = self.queryset.only('ghazal_content')
        # serializedData = GhazalsSerializer(data=self.queryset,many=True, fields = fields)
        #self.queryset #.get_cleaned_content()
        # data = getattr(self.queryset,'ghazal_content')[0]
        # print(data)
        # queryset = self.queryset
        # print(serializedData)
        # return serializedData
        # if serializedData.is_valid():
        #     return  Response(data =serializedData,status = status.HTTP_200_OK)
        # return Response(status = status.HTTP_400_BAD_REQUEST)
        temp = self.queryset.only('cleaned_content').first()
        print(temp.author_alphabet)
        return Response(self.queryset)
