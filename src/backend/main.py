from pathlib import Path
from typing import Union
from PIL import Image
import os
from dotenv import load_dotenv

from google.cloud import vision
from google.oauth2 import service_account
from openai import OpenAI

from backend.ocr import google_vision
from streamlit.runtime.uploaded_file_manager import UploadedFile
from backend.modules.extract_items import OpenaiItemExtractor

load_dotenv(verbose=True)

CREDENTIAL = service_account.Credentials.from_service_account_file("../key.json")
GOOGLECLIENT = vision.ImageAnnotatorClient(credentials=CREDENTIAL)

os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")
OPENAI_CLIENT = OpenAI()


def detect(jpeg_file: Union[UploadedFile, Image.Image]) -> str:
    google_vision_detecter = google_vision.GoogleVisionDetecter(GOOGLECLIENT)
    response = google_vision_detecter.detect_text(jpeg_file)
    return response


def extract_items(text: str) -> dict[str, dict[str, any]]:
    openai_item_extractor = OpenaiItemExtractor(OPENAI_CLIENT)
    return openai_item_extractor.extract_items(text)
