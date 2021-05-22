import argparse

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from AI.tile_predict import tile_predict
from main.forms import InputForm
from main.models import Search
from main.serializers import SearchSerializer


def ShowResult(request):
    if request.method == 'POST':
        form = InputForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save()
            print(data.Image)
            path = str(data.Image).split('.')[0]
            print(path)
            # AI 돌려서 result 얻기
            result = tile_predict("unet_min", [256,256,3], "E:\\JXS\\Seoul1ro\\AI\\unet_mini300_06_07_20.hdf5", path, "tiff", "output/", 3, 8)

            # result = Search.objects.last()
            print(result) # None
            return render(request, 'main/index.html', {
                'form': form,
                'result': result,
            })
        else:
            # 올바른 파일 올려달라고 메세지 넣기
            form = InputForm()
            return render(request, 'main/index.html', {
                'form': form,
            })

    # GET
    else:
        form = InputForm()
        return render(request, 'main/index.html', {
            'form': form,
        })


class SendtoAIView(viewsets.ModelViewSet):
    serializer_class = SearchSerializer
    queryset = Search.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)