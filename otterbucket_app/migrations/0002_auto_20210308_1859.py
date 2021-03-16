# Generated by Django 3.1.7 on 2021-03-09 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('otterbucket_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bucketitem',
            old_name='item_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='bucketitem',
            old_name='item_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='bucketitem',
            old_name='item_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='bucketlist',
            old_name='bucket_item_id',
            new_name='bucket_item',
        ),
        migrations.RenameField(
            model_name='bucketlist',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_id',
            new_name='id',
        ),
    ]
