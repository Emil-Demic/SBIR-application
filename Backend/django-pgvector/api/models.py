from django.db import models
from pgvector.django import VectorField

# Create your models here.

class Embedding(models.Model):
    embedding = VectorField(dimensions=768)
    img_id = models.IntegerField()
    