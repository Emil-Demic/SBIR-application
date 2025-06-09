import boto3

s3 = boto3.client('s3')
s3.download_file('<NAME OF S3 BUCKET>', '<MODEL FILE>', './api/model.onnx')
s3.download_file('<NAME OF S3 BUCKET>', '<PRECOMPUTED EMBEDDINGS OF IMAGES>', './api/embeddings.npy')
