from django.db import models
from django.core.validators import FileExtensionValidator


class Texts(models.Model):
    instruction = models.CharField(max_length=30)
    ref_no = models.CharField(max_length=30)


class Image(models.Model):
    img = models.ForeignKey(Texts, on_delete=models.CASCADE)
    image = models.FileField(blank=False, null=False, upload_to='file',validators=[FileExtensionValidator(['pdf','jpg','gif','jpeg','bmp','ai','eps'])])

    def __str__(self):
        return "{} : {}".format(self.img.instruction,  self.image.name ,self.img.ref_no)
