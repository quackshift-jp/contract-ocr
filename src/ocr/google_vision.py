from google.cloud import vision
import io
from google.cloud.vision_v1 import AnnotateImageResponse
import json
from models.text_detecter import TextDetecter


class GoogleVisionDetecter(TextDetecter):
    def __init__(self, client):
        self.client = client

    def read_image(self, image_path: str) -> vision.Image:
        # TODO:try-exceptのエラーハンドリングも導入する
        with io.open(image_path, "rb") as image_file:
            content = image_file.read()
        return vision.Image(content=content)

    def extract_text(self, response: AnnotateImageResponse) -> str:
        json_response = json.loads(AnnotateImageResponse.to_json(response))
        return json_response["fullTextAnnotation"]["text"].replace("\n", "")

    def detect_text(self, image_path: str) -> str:
        image = self.read_image(image_path)
        response = self.client.document_text_detection(
            image=image, image_context={"language_hints": ["ja"]}
        )
        return self.extract_text(response)
