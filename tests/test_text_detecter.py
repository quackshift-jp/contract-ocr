from models.text_detecter import TextDetecter


class MyTestClass(TextDetecter):
    def __init__(self):
        pass

    def read_image(self, image_path="テストパス"):
        return "TextDetecterの継承1"

    def detect_text(self, image="テストイメージ"):
        return "TextDetecterの継承2"


def test_text_detecter():
    obj = MyTestClass()
    assert obj.read_image() == "TextDetecterの継承1"
    assert obj.detect_text() == "TextDetecterの継承2"
