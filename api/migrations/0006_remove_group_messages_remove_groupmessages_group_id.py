# Generated by Django 4.1 on 2022-09-11 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_group_messages_alter_groupmessages_group_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='messages',
        ),
        migrations.RemoveField(
            model_name='groupmessages',
            name='group_id',
        ),
    ]
