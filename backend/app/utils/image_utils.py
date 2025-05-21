from PIL import Image
from fastapi import UploadFile

def read_imagefile(file: UploadFile) -> Image.Image:
    image = Image.open(file.file)
    return image.convert("RGB") 