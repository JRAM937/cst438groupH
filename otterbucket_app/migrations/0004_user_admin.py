
# Generated by Django 3.1.7 on 2021-03-26 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otterbucket_app', '0003_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='admin',
            field=models.BooleanField(default=False),
        ),
    ]

