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
        self.session = InferenceSession("model.onnx")

        gallery_embeddings = np.load("embeddings.npy").squeeze()
        self.index = IndexFlatL2(gallery_embeddings.shape[1])
        self.index.add(gallery_embeddings)
        
        mean=[0.48145466, 0.4578275, 0.40821073]
        std=[0.26862954, 0.26130258, 0.27577711]
        self.mean = np.array(mean, dtype=np.float32).reshape(3, 1, 1)
        self.std = np.array(std, dtype=np.float32).reshape(3, 1, 1)

        # number of image to return
        self.k = 50

    def decode_request(self, request):
        image = request['image']
        image = image[image.find(",")+1:]
        image = Image.open(BytesIO(b64decode(image)))
        image = image.resize((224, 224), resample=Image.BICUBIC).convert("RGB")
        image = np.array(image, dtype=np.float32).transpose(2, 0, 1) / 255.0
        image =  (image - self.mean) / self.std
        return np.expand_dims(image, axis=0)
    
    def predict(self, image):
        return self.session.run(None, {'data': image})
    
    def encode_response(self, output):
        _, I = self.index.search(output[0], self.k)
        return {"body": I[0].tolist()}
        

if __name__ == "__main__":
    api = SBIR_API()
    cors_middleware = (
        CORSMiddleware, 
        {
            "allow_origins": ["*"],
            "allow_methods": ["GET", "POST"],
            "allow_headers": ["content-type"],
        }
    )
    server = LitServer(api, middlewares=[cors_middleware])
    server.run(port=8000)
