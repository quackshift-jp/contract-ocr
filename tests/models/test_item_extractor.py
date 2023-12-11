from backend.models.item_extractor import ItemExtractor


class MyTestClass(ItemExtractor):
    def __init__(self) -> None:
        pass

    def extract_items(self, text: str = "テスト") -> dict[str, dict[str, any]]:
        return {"content": {"物件名": "テスト物件", "賃料": 999, "契約日": "テスト契約日"}}


def test_item_extractor():
    obj = MyTestClass()
    obj.extract_items("テスト") == {
        "content": {"物件名": "テスト物件", "賃料": 999, "契約日": "テスト契約日"}
    }
