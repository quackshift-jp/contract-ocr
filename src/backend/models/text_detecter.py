from abc import abstractmethod, ABC
from google.cloud import vision


class TextDetecter(ABC):
    def __init__(self, client: vision.ImageAnnotatorClient):
        self.client = client

    @abstractmethod
    def read_image(self, image_path: str) -> any:
        """画像の読み込みメソッド
        args:
            image_path str: 読み込み対象となる画像が存在しているパス
        return:
            any: 各APIのOCRメソッドに適した画像情報(Google Visionの場合は、vision.Image型を返す必要がある)
        """
        raise NotImplementedError()

    @abstractmethod
    def detect_text(self, image_path: str) -> str:
        """OCRのテキスト検知メソッド
        args:
            image any: 各APIのOCRメソッドに適した画像情報
        return:
            str: 識別された文字情報
        """
        raise NotImplementedError()
