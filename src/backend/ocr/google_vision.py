from typing import Union
import io
import json
from PIL import Image

from google.cloud import vision
from google.cloud.vision_v1 import AnnotateImageResponse

from backend.models.text_detecter import TextDetecter
from streamlit.runtime.uploaded_file_manager import UploadedFile


class GoogleVisionDetecter(TextDetecter):
    def __init__(self, client):
        self.client = client

    def read_image(self, jpeg_file: Union[UploadedFile, Image.Image]) -> vision.Image:
        if isinstance(jpeg_file, UploadedFile):
            content = jpeg_file.read()
        else:
            img_byte_arr = io.BytesIO()
            jpeg_file.save(img_byte_arr, format="JPEG")
            content = img_byte_arr.getvalue()
        return vision.Image(content=content)

    def extract_text(self, response: AnnotateImageResponse) -> str:
        json_response = json.loads(AnnotateImageResponse.to_json(response))
        return json_response["fullTextAnnotation"]["text"].replace("\n", "")

    def detect_text(self, jpeg_file: UploadedFile) -> str:
        if isinstance(jpeg_file, UploadedFile):
            image = self.read_image(jpeg_file)
            response = self.client.document_text_detection(
                image=image, image_context={"language_hints": ["ja"]}
            )
            return self.extract_text(response)
        texts = []
        for file in jpeg_file:
            image = self.read_image(file)
            response = self.client.document_text_detection(
                image=image, image_context={"language_hints": ["ja"]}
            )
            text = self.extract_text(response)
            texts.append(text)
        return "\n".join(texts)
