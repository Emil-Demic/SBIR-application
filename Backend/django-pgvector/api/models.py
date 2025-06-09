from django.db import models
from pgvector.django import VectorField


class Embedding(models.Model):
    # Model repersenting the embedding and the id of an image in the gallery
    embedding = VectorField(dimensions=768)
    img_id = models.IntegerField()
    