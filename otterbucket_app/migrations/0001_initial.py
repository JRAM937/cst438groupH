# Generated by Django 3.1.7 on 2021-03-09 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BucketItem',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_title', models.CharField(max_length=200)),
                ('item_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BucketList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bucket_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otterbucket_app.bucketitem')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otterbucket_app.user')),
            ],
        ),
    ]
