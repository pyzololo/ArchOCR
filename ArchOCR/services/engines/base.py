from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, Dict, Any
from PIL import Image


@dataclass
class OcrResult:
    text: str
    confidence: Optional[float] = None
    meta: Optional[Dict[str, Any]] = None


class BaseOcrEngine(ABC):
    name: str = "base"

    @abstractmethod
    def recognize(self, image: Image.Image) -> OcrResult:
        ...
