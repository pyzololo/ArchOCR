from typing import Optional, Dict
from PIL import Image
from django.core.files.storage import default_storage
from django.db import transaction

from . import ENGINE_REGISTRY, DEFAULT_ENGINE
from .preprocessing import simple_threshold
from ..models import ScanPage, Translation


class OcrService:
    def __init__(self):
        self._cache: Dict[str, object] = {}

    def _get_engine(self, name: Optional[str]):
        name = name or DEFAULT_ENGINE
        if name not in ENGINE_REGISTRY:
            name = DEFAULT_ENGINE
        if name not in self._cache:
            self._cache[name] = ENGINE_REGISTRY[name]()  # instancja silnika
        return self._cache[name]

    @transaction.atomic
    def run(self, page: ScanPage, model_name: Optional[str] = None, use_threshold: bool = True) -> Translation:
        # 1) wczytaj obraz z magazynu
        with default_storage.open(page.image.name, "rb") as f:
            img = Image.open(f).convert("RGB")

        # 2) preprocessing
        if use_threshold:
            img = simple_threshold(img)

        # 3) rozpoznanie
        engine = self._get_engine(model_name)
        result = engine.recognize(img)

        # 4) zapis do bazy
        tr = Translation.objects.create(
            page=page,
            model_name=engine.name,
            text=result.text,
        )
        return tr


ocr_service = OcrService()
