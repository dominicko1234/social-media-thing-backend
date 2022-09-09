from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *

# Create your views here.

def main(*args, **kwargs):
    return HttpResponse('testing')


class GroupView(APIView):
    serializer_class = GroupSerializer

    def get(self, request):
        output = [{"id": output.id, "messages": output.messages} for output in Group.objects.order_by('-date_posted')]
        return Response(output)

    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)

    def delete(self,request):
        pass