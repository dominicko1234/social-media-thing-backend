from rest_framework import serializers
from .models import Group

class GroupSerializer(serializers.ModelSerializer):
    model = Group
    fields = {'id', 'messages'}