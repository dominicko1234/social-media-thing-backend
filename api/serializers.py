from rest_framework import serializers
from .models import Group, GroupMessages

class GroupSerializer(serializers.ModelSerializer):
    model = Group
    fields = {'id', 'group_name' 'messages'}

class GroupMessagesSerializer(serializers.ModelSerializer):
    model = GroupMessages
    fields = {'date_posted', 'message'}