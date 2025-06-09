from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Embedding
from PIL import Image
from io import BytesIO
from base64 import b64decode
from onnxruntime import InferenceSession
from pgvector.django import L2Distance

import numpy as np


session = InferenceSession("/home/ec2-user/backend/api/model.onnx")
gallery_embeddings = np.load("/home/ec2-user/backend/api/embeddings.npy")

mean=[0.485, 0.456, 0.406]
std=[0.229, 0.224, 0.225]
mean = np.array(mean, dtype=np.float32).reshape(3, 1, 1)
std = np.array(std, dtype=np.float32).reshape(3, 1, 1)

# Create your views here.

@api_view(["POST"])
def predict(request):
    image = request.data['image']
    image = image[image.find(",")+1:]
    image = Image.open(BytesIO(b64decode(image)))
    image = image.resize((224, 224), resample=Image.BICUBIC).convert("RGB")
    image = np.array(image, dtype=np.float32).transpose(2, 0, 1) / 255.0
    image =  (image - mean) / std
    image = np.expand_dims(image, axis=0)
    image_embedding = session.run(None, {'data': image})
    predictions = Embedding.objects.order_by(L2Distance('embedding', image_embedding[0].squeeze()))
    predictions = [pred.img_id for pred in predictions]
    return Response(predictions)
    

