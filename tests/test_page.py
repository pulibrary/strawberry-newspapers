from pathlib import Path
from newspaper.models.pages import Page
import PIL
from lxml import etree

def test_page_image(shared_datadir):
    sample_file = shared_datadir / "test_image.jpg"
    page:Page = Page(sample_file)
    assert Path(page._img_path).is_file

    assert page.image.__class__ is PIL.JpegImagePlugin.JpegImageFile


def test_page_text(shared_datadir):
    sample_file = shared_datadir / "test_image.jpg"
    page:Page = Page(sample_file)

    assert page.text.__class__ is str


def test_page_xml(shared_datadir):
    sample_file = shared_datadir / "test_image.jpg"
    page:Page = Page(sample_file)

    assert type(page.xml) is etree._Element


