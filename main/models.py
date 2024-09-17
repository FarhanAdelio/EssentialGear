import uuid
from django.db import models
# Create your models here.

class GearEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(max_length=300)
    stock = models.IntegerField()
    rating = models.IntegerField()