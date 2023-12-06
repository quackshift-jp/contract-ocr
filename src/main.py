from pathlib import Path
from google.cloud import vision
from google.oauth2 import service_account
from ocr import google_vision
from modules import pdf_to_image

GOOGLE_DRIVE_PATH = Path("/Users/apple/Google Drive/マイドライブ/pj-takase")
CREDENTIAL = service_account.Credentials.from_service_account_file("../key.json")
CLIENT = vision.ImageAnnotatorClient(credentials=CREDENTIAL)

pdf_to_image.convert_pdf_to_images(GOOGLE_DRIVE_PATH, "./images", "図面")

google_vision_detecter = google_vision.GoogleVisionDetecter(CLIENT)

output = google_vision_detecter.detect_text("images/202791　図面0001-1.jpg")
print(output)
