import re
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import Group, GroupMessages

# Create your views here.

def main(*args, **kwargs):
    return HttpResponse('testing')


class GroupView(APIView):
    serializer_class = GroupSerializer

    def get(self, request):
        output = [{"id": output.id, "group_name": output.group_name} for output in Group.objects.all()]
        return Response(output)

    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self,request):
        pass

class GroupMessagesView(APIView):
    serializer_class = GroupMessagesSerializer

    def get(self, request):
        output = [{"date_posted": output.date_posted, "message": output.message} for output in GroupMessages.objects.order_by('-date_posted')]
        return Response(output)

    def post(self, request):
        serializer = GroupMessagesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)