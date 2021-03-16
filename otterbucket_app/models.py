
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key = True)
    username = models.CharField(max_length=50)
    def __str__(self):
        return self.username

class BucketItem(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    def __str__(self):
        return self.title + ": " + self.text
    
class BucketList(models.Model):
    user = models.ForeignKey('user',on_delete=models.CASCADE)
    bucket_item = models.ForeignKey('BucketItem', on_delete=models.CASCADE)
    def __str__(self):
        return "user: " + self.user_id + ", bucket item: " + self.bucket_item_id