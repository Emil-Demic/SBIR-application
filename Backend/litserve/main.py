import numpy as np

from litserve import LitAPI, LitServer
from PIL import Image
from io import BytesIO
from base64 import b64decode
from onnxruntime import InferenceSession
from starlette.middleware.cors import CORSMiddleware
from faiss import IndexFlatL2


class SBIR_API(LitAPI):
    def setup(self, device):       
        # Load the model 
        self.session = InferenceSession("model.onnx")

        # Load image embedding and construct an index to speed up the search
        gallery_embeddings = np.load("embeddings.npy").squeeze()
        self.index = IndexFlatL2(gallery_embeddings.shape[1])
        self.index.add(gallery_embeddings)
        
        # Define the mean and std values for normalization
        mean=[0.48145466, 0.4578275, 0.40821073]
        std=[0.26862954, 0.26130258, 0.27577711]
        self.mean = np.array(mean, dtype=np.float32).reshape(3, 1, 1)
        self.std = np.array(std, dtype=np.float32).reshape(3, 1, 1)

        # Set the number of images to return
        self.k = 60

    def decode_request(self, request):
        # Load the query image from request
        image = request['image']
        image = image[image.find(",")+1:]
        image = Image.open(BytesIO(b64decode(image)))
        
        # Resize the image and convert to RGB
        image = image.resize((224, 224), resample=Image.BICUBIC).convert("RGB")
        # Transpose to array to match the dimesions of the model 
        # and scale image values to values between 0 and 1
        image = np.array(image, dtype=np.float32).transpose(2, 0, 1) / 255.0
        # Normalize the image with the defined mean and std values
        image =  (image - self.mean) / self.std
        # Unsqueeze the array to match model dimensions
        return np.expand_dims(image, axis=0)
    
    def predict(self, image):
        # Calculate the embedding of the query
        return self.session.run(None, {'data': image})
    
    def encode_response(self, output):
        # Find k images with the smallest L2 distance to the query
        _, I = self.index.search(output[0], self.k)
        return I[0].tolist()
        

if __name__ == "__main__":
    # Set server parameters and run it
    api = SBIR_API()
    cors_middleware = (
        CORSMiddleware, 
        {
            "allow_origins": ["https://app.sbir.superpowered-nutball.xyz", "https://www.app.sbir.superpowered-nutball.xyz"]
            "allow_methods": ["GET", "POST"],
            "allow_headers": ["content-type"],
        }
    )
    server = LitServer(api, middlewares=[cors_middleware])
    server.run(port=8000)
