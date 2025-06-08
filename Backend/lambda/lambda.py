import base64
import json
import io
from PIL import Image
import numpy as np
import onnxruntime
import boto3

s3 = boto3.client('s3')
s3.download_file('<NAME OF S3 BUCKET>', '<MODEL FILE>', '/tmp/model.onnx')
s3.download_file('<NAME OF S3 BUCKET>', '<PRECOMPUTED EMBEDDINGS OF IMAGES>', '/tmp/embeddings.npy')

session = onnxruntime.InferenceSession("/tmp/model.onnx")
gallery_embeddings = np.load("/tmp/embeddings.npy")

mean=[0.485, 0.456, 0.406]
std=[0.229, 0.224, 0.225]
mean = np.array(mean, dtype=np.float32).reshape(3, 1, 1)
std = np.array(std, dtype=np.float32).reshape(3, 1, 1)

def lambda_handler(event, context):
    try:
        image = event['body']
        image = json.loads(image)['image']
        image = image[image.find(",")+1:]
        image = Image.open(io.BytesIO(base64.b64decode(image)))
        image = image.resize((224, 224), resample=Image.Resampling.BILINEAR).convert("RGB")
        image = np.array(image, dtype=np.float32) / 255.
        image = image.transpose(2, 0, 1)
        image =  (image - self.mean) / self.std
        image = np.expand_dims(image, 0)

        embedding = session.run(None, {'data': image})[0]

        similarities = np.zeros(3000)
        for i in range(3000):
            similarities[i] = np.linalg.norm(embedding - gallery_embeddings[i])
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
