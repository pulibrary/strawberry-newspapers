from pathlib import Path
from PIL import Image
import pytesseract


class Page():
    def __init__(self, img_path: str) -> None:
        self._img_path:str = img_path
        self._image = None
        self._text = None
        self._xml = None        

    @property
    def image(self):
        if self._image is None:
            self._image = Image.open(self._img_path)
        return self._image

    @property
    def text(self) -> str:
        if self._text is None:
            self._text = pytesseract.image_to_string(self.image)
        return self._text

    @property
    def xml(self) -> str:
        if self._xml is None:
            self._xml = pytesseract.image_to_alto_xml(self.image)
        return self._xml

    
