from django.db import models

def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, "images")

class NotanLevelChoice(models.IntegerChoices):
    TWO = 2, 'two'
    THREE = 3, 'three'
    FOUR = 4, 'four'

class SqImage(models.Model):
    is_grey = models.BooleanField(default=True)
    image_path = models.FilePathField(path=images_path)
    notan_levels = models.IntegerField(default=NotanLevelChoice.TWO, choices=NotanLevelChoice.choices)
    posterize_level = models.IntegerField(default=3)
    blur_level = models.IntegerField(default=7)
    output_file_format  = models.CharField(max_length = 200, default= '.png')



