from django.db import models

# Create your models here.
class BucketList(models.Model):
    user_id = models.integerField
    bucket_item_id = models.ForeignKey('BucketItem', on_delete=models.CASCADE)
    
class BucketItem(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_title = models.CharField(max_Length=200)
    item_text = models.TextField()