# Generated by Django 4.1 on 2022-09-11 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_group_messages_remove_groupmessages_group_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='messages',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.groupmessages'),
        ),
        migrations.AddField(
            model_name='groupmessages',
            name='group_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.group'),
        ),
    ]
