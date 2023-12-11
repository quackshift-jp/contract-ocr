from backend.ocr.google_vision import GoogleVisionDetecter, AnnotateImageResponse
from google.cloud import vision
from streamlit.runtime.uploaded_file_manager import UploadedFile


def test_google_vision_detecter(monkeypatch):
    class MockClient:
        def document_text_detection(self, image, image_context):
            return AnnotateImageResponse()

    def mock_read_image(self, image_path: str) -> vision.Image:
        return vision.Image(content="テスト画像")

    def mock_extract_text(self, response: AnnotateImageResponse) -> str:
        return "テスト"

    monkeypatch.setattr(GoogleVisionDetecter, "read_image", mock_read_image)
    monkeypatch.setattr(GoogleVisionDetecter, "extract_text", mock_extract_text)

    detector = GoogleVisionDetecter(MockClient())

    actual_1 = detector.inference(["テストjpeg画像1", "テストjpeg画像2"])
    actual_2 = detector.inference(["テストjpeg画像"])
    assert actual_1 == "テスト\nテスト"
    assert actual_2 == "テスト"
