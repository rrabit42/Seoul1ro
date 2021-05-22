from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.forms import InputForm
from main.models import Search
from main.serializers import SearchSerializer


def ShowResult(request):
    if request.method == 'POST':
        form = InputForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save()
            print(data.scale)
            print(data.area)
            print(data.Image)
            # AI 돌려서 result 얻기
            result = Search.objects.last()
            print(result)
            return render(request, 'main/index.html', {
                'form': form,
                'result': result,
            })
        else:
            form = InputForm()
            return render(request, 'main/index.html', {
                'form': form,
            })

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