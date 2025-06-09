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

# Load the model 
session = InferenceSession("./api/model.onnx")

# Define the mean and std values for normalization
mean=[0.485, 0.456, 0.406]
std=[0.229, 0.224, 0.225]
mean = np.array(mean, dtype=np.float32).reshape(3, 1, 1)
std = np.array(std, dtype=np.float32).reshape(3, 1, 1)


@api_view(["POST"])
def predict(request):
    # Load the query image from request
    image = request.data['image']
    image = image[image.find(",")+1:]
    image = Image.open(BytesIO(b64decode(image)))

    # Resize the image and convert to RGB
    image = image.resize((224, 224), resample=Image.BICUBIC).convert("RGB")
    # Transpose to array to match the dimesions of the model 
    # and scale image values to values between 0 and 1
    image = np.array(image, dtype=np.float32).transpose(2, 0, 1) / 255.0
    # Normalize the image with the defined mean and std values
    image =  (image - mean) / std
    # Unsqueeze the array to match model dimensions
    image = np.expand_dims(image, axis=0)

    # Calculate the embedding of the query
    image_embedding = session.run(None, {'data': image})

    # Sort the images in gallery based on L2 distance to the query
    predictions = Embedding.objects.order_by(L2Distance('embedding', image_embedding[0].squeeze()))
    # Parse ids of images to a list 
    predictions = [pred.img_id for pred in predictions]
    return Response(predictions)
    

