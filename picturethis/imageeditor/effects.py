import os
from PIL import Image, ImageFilter, ImageOps, ImageEnhance

from picturethis import settings


class ImageEffects(object):
    """Handle image effects and filters."""

    def __init__(self, image, effect):
        """Initialize image effects class."""
        self.image = Image.open(image)
        self.effect = effect
        self.image_name = image.name
        path = settings.MEDIA_ROOT + '/editedphotos/'
        if not os.path.exists(path):
            os.makedirs(path)
        self.file_path = path + \
            effect + os.path.basename(self.image_name)

    def filters(self):
        """Handle Filters on images."""
        if self.effect == 'blur':
            to_save = self.image.filter(ImageFilter.BLUR)
        if self.effect == 'contour':
            to_save = self.image.filter(ImageFilter.CONTOUR)
        if self.effect == 'emboss':
            to_save = self.image.filter(ImageFilter.EMBOSS)
        if self.effect == 'detail':
            to_save = self.image.filter(ImageFilter.DETAIL)
        if self.effect == 'smooth':
            to_save = self.image.filter(ImageFilter.SMOOTH)
        if self.effect == 'sharpen':
            to_save = self.image.filter(ImageFilter.SHARPEN)
        to_save.save(self.file_path)
        return self.file_path

    def operations(self):
        """Handle other simple image operations."""
        if self.effect == 'flip':
            to_save = ImageOps.flip(self.image)
        if self.effect == 'mirror':
            to_save = ImageOps.mirror(self.image)
        if self.effect == 'invert':
            to_save = ImageOps.invert(self.image)
        if self.effect == 'grayscale':
            to_save = ImageOps.grayscale(self.image)
        to_save.save(self.file_path)
        return self.file_path
