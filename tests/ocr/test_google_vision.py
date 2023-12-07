from backend.ocr.google_vision import GoogleVisionDetecter, AnnotateImageResponse
from google.cloud import vision


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

    actual = detector.detect_text("テストパス")
    assert actual == "テスト"
