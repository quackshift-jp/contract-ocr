from backend.models.text_detecter import TextDetector


class MyTestClass(TextDetector):
    def __init__(self):
        pass

    def read_image(self, jpeg_file="テストイメージ"):
        return "TextDetecterの継承1"

    def detect_text(self, jpeg_file="テストイメージ"):
        return "TextDetecterの継承2"


def test_text_detecter():
    obj = MyTestClass()
    assert obj.read_image() == "TextDetecterの継承1"
    assert obj.detect_text() == "TextDetecterの継承2"
