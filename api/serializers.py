from rest_framework import serializers
from .models import Group, GroupMessages

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'group_name']

class GroupMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMessages
        fields = ['date_posted', 'message']