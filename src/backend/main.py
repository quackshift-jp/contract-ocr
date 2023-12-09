from pathlib import Path
from typing import Union
from PIL import Image

from google.cloud import vision
from google.oauth2 import service_account

from backend.ocr import google_vision
from streamlit.runtime.uploaded_file_manager import UploadedFile

CREDENTIAL = service_account.Credentials.from_service_account_file("../key.json")
CLIENT = vision.ImageAnnotatorClient(credentials=CREDENTIAL)


def detect(jpeg_file: Union[UploadedFile, Image.Image]) -> str:
    google_vision_detecter = google_vision.GoogleVisionDetecter(CLIENT)
    response = google_vision_detecter.detect_text(jpeg_file)
    return response
