from .base import BaseOcrEngine, OcrResult
from PIL import Image


class DummyEngine(BaseOcrEngine):
    name = "baseline"

    def recognize(self, image: Image.Image) -> OcrResult:
        w, h = image.size
        return OcrResult(text=f"[Dummy OCR] size={w}x{h}")
