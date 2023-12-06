from abc import abstractmethod, ABC


class TextDetecter(ABC):
    def __init__(self):
        pass

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
    def detect_text(self, image: any) -> str:
        """OCRのテキスト検知メソッド
        args:
            image any: 各APIのOCRメソッドに適した画像情報
        return:
            識別された文字情報
        return
        """
        raise NotImplementedError()
