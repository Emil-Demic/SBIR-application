import base64
import json
import io
from PIL import Image
import numpy as np
import onnxruntime
import boto3

# Download the model file and image embeddings
s3 = boto3.client('s3')
s3.download_file('<NAME OF S3 BUCKET>', '<MODEL FILE>', '/tmp/model.onnx')
s3.download_file('<NAME OF S3 BUCKET>', '<PRECOMPUTED EMBEDDINGS OF IMAGES>', '/tmp/embeddings.npy')

# Load the model and the embeddings
session = onnxruntime.InferenceSession("/tmp/model.onnx")
gallery_embeddings = np.load("/tmp/embeddings.npy")

# Define the mean and std values for normalization
mean=[0.485, 0.456, 0.406]
std=[0.229, 0.224, 0.225]
mean = np.array(mean, dtype=np.float32).reshape(3, 1, 1)
std = np.array(std, dtype=np.float32).reshape(3, 1, 1)

def lambda_handler(event, context):
    try:
        # Load the query image from request
        image = event['body']
        image = json.loads(image)['image']
        image = image[image.find(",")+1:]
        image = Image.open(io.BytesIO(base64.b64decode(image)))

        # Resize the image and convert to RGB
        image = image.resize((224, 224), resample=Image.Resampling.BILINEAR).convert("RGB")
        # Scale image values to values between 0 and 1
        image = np.array(image, dtype=np.float32) / 255.
        # Transpose to array to match the dimesions of the model
        image = image.transpose(2, 0, 1)
        # Normalize the image with the defined mean and std values
        image =  (image - mean) / std
        # Unsqueeze the array to match model dimensions
        image = np.expand_dims(image, 0)

        # Calculate the embedding of the query
        embedding = session.run(None, {'data': image})[0]

        # Calculate the L2 distance to all images in the gallery
        similarities = np.zeros(3000)
        for i in range(3000):
            similarities[i] = np.linalg.norm(embedding - gallery_embeddings[i])

        # Find the images closest to the query
        top_k_indices = np.argsort(similarities).tolist()

        return {
            "statusCode": 200,
            "body": json.dumps(top_k_indices)
        }
        
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
