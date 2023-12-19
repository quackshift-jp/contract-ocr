import cv2
from pathlib import Path
from PIL import Image
import layoutparser as lp
from layoutparser.models import Detectron2LayoutModel

from layoutparser.elements.layout import Layout


def create_parse_model(config_path: str, model_path: str) -> Detectron2LayoutModel:
    """
    config_path: "lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config"
    model_path: "path/to/model_final.pth"
    """
    return lp.Detectron2LayoutModel(
        config_path,
        model_path=model_path,
        extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.8],
        label_map={0: "Text", 1: "Title", 2: "List", 3: "Table", 4: "Figure"},
    )


def detect_layout(image_path: str, model_path: str) -> Layout:
    image = cv2.imread(image_path)
    model = create_parse_model(
        "lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config", model_path
    )

    layout = model.detect(image)
    return layout


def crop_text_blocks(image_path, layout: Layout) -> list[Image.Image]:
    text_blocks = [b for b in layout if b.type == "Text"]
    image = Image.open(image_path)
    cropped_images = []

    for block in text_blocks:
        # ブロックの座標を取得
        rectangle = block.block
        left, top, right, bottom = (
            rectangle.x_1,
            rectangle.y_1,
            rectangle.x_2,
            rectangle.y_2,
        )

        # 画像を切り出す
        cropped_image = image.crop((left, top, right, bottom))
        cropped_images.append(cropped_image)

    return cropped_images
