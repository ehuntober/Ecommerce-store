from django.db import models

# Create your models here.

from django.contrib.auth.models import User 
from django.contenttypes.models import ContentType 
from django.contenttypes.fields import GenericForeignKey 

class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

