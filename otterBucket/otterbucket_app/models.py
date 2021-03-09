from django.db import models

# Create your models here.
class user(models.Model):
    user_id = models.AutoField(primary_key = True)
    username = models.CharField(max_Length=50)

class BucketItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_title = models.CharField(max_Length=200)
    item_text = models.TextField()
    
class BucketList(models.Model):
    user_id = models.ForeignKey('user',on_delete=models.CASCADE)
    bucket_item_id = models.ForeignKey('BucketItem', on_delete=models.CASCADE)