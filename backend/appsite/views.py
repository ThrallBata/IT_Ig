from django.http import HttpResponseNotFound
from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .utils import *
from .models import *
from .serializers import ProjectSerializer


class ProjectAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)



def index(request):

    return render(request, 'appsite/index.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
