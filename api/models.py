from tkinter import CASCADE
from django.db import models
import uuid

# Create your models here.

class Group(models.Model):
    id = models.CharField(primary_key=True, null=False, max_length=36)
    group_name = models.CharField(null=False, max_length=30)
    # messages = models.ForeignKey('GroupMessages', on_delete=models.CASCADE)

    #remember to add username in User model as a max_length of 20

    usernames = models.CharField(null=False, max_length=20)

class GroupMessages(models.Model):
    # group_id = models.ForeignKey('Group', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    message = models.TextField(null=False)