from PIL import Image, ImageOps


def to_grayscale(img: Image.Image) -> Image.Image:
    return ImageOps.grayscale(img)


def simple_threshold(img: Image.Image, thresh: int = 180) -> Image.Image:
    g = to_grayscale(img)
    return g.point(lambda p: 255 if p > thresh else 0)
