# Generated by Django 4.1.7 on 2023-05-10 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_is_request'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_request',
        ),
        migrations.AddField(
            model_name='friend',
            name='is_request',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]