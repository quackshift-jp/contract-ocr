from typing import Union
from PIL import Image
import io
import datetime
from PIL.PpmImagePlugin import PpmImageFile

import boto3
from streamlit.runtime.uploaded_file_manager import UploadedFile


S3_CLIENT = boto3.client("s3")
DATETIME = datetime.date.today()


def upload_streamlit_file_to_s3(
    streamlit_file: Union[list[PpmImageFile], UploadedFile],
    bucket_name: str,
    key: str,
) -> None:
    if isinstance(streamlit_file, list):
        streamlit_file = get_concat_image(streamlit_file)

    S3_CLIENT.put_object(
        Body=streamlit_file,
        Bucket=bucket_name,
        Key=f"{DATETIME}/{key}.jpeg",
    )


def get_concat_image(image_list: list[PpmImageFile]) -> bytes:
    widths, heights = zip(*(image.size for image in image_list))
    max_width = max(widths)
    total_height = sum(heights)

    concat_image = Image.new("RGB", (max_width, total_height))

    y_offset = 0
    for im in image_list:
        concat_image.paste(im, (0, y_offset))
        y_offset += im.size[1]

    return convert_pil_to_bytes(concat_image)


def convert_pil_to_bytes(pil_file: Image.Image) -> bytes:
    img_byte_arr = io.BytesIO()
    pil_file.save(img_byte_arr, format="JPEG")
    return img_byte_arr.getvalue()
