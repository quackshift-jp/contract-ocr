from abc import abstractmethod, ABC
from typing import Union
from PIL import Image

from streamlit.runtime.uploaded_file_manager import UploadedFile
from google.cloud import vision


class TextDetector(ABC):
    def __init__(self, client: vision.ImageAnnotatorClient):
        self.client = client

    @abstractmethod
    def read_image(self, jpeg_file: Union[UploadedFile, Image.Image]) -> vision.Image:
        """画像の読み込みメソッド
        args:
            jpeg_file Union[UploadedFile, Image.Image]: 読み込み対象となるjpeg画像
        return:
            any: 各APIのOCRメソッドに適した画像情報(Google Visionの場合は、vision.Image型を返す必要がある)
        """
        raise NotImplementedError()

    @abstractmethod
    def detect_text(self, jpeg_file: Union[UploadedFile, Image.Image]) -> str:
        """OCRのテキスト検知メソッド
        args:
            jpeg_file Union[UploadedFile, Image.Image]: 各APIのOCRメソッドに適したjpeg画像情報
        return:
            str: 識別された文字情報
        """
        raise NotImplementedError()
