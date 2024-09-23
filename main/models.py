import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GearEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(max_length=300)
    stock = models.IntegerField()
    rating = models.IntegerField()