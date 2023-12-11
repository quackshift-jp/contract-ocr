from typing import Union
import io
import json
from PIL import Image

from google.cloud import vision
from google.cloud.vision_v1 import AnnotateImageResponse

from backend.models.text_detecter import TextDetector
from streamlit.runtime.uploaded_file_manager import UploadedFile


class GoogleVisionDetecter(TextDetector):
    def __init__(self, client):
        self.client = client

    def read_image(self, jpeg_file: Union[UploadedFile, Image.Image]) -> vision.Image:
        # streamlitのUploadedFileは、UploadedFile.read()でバイトオブジェクトを取得できる
        if isinstance(jpeg_file, UploadedFile):
            content = jpeg_file.read()
        else:
            # PIL.Imageは、jpegとして保存してバイト列を取り出す必要がある
            img_byte_arr = io.BytesIO()
            jpeg_file.save(img_byte_arr, format="JPEG")
            content = img_byte_arr.getvalue()
        return vision.Image(content=content)

    def detect_text(self, image: vision.Image) -> AnnotateImageResponse:
        response = self.client.document_text_detection(
            image=image, image_context={"language_hints": ["ja"]}
        )
        return response

    def extract_text(self, response: AnnotateImageResponse) -> str:
        json_response = json.loads(AnnotateImageResponse.to_json(response))
        return json_response["fullTextAnnotation"]["text"].replace("\n", "")

    def inference(self, jpeg_file: Union[UploadedFile, list[Image.Image]]) -> str:
        if isinstance(jpeg_file, UploadedFile):
            image = self.read_image(jpeg_file)
            response = self.detect_text(image)
            return self.extract_text(response)
        texts = []
        for file in jpeg_file:
            image = self.read_image(file)
            response = self.detect_text(image)
            text = self.extract_text(response)
            texts.append(text)
        return "\n".join(texts)
