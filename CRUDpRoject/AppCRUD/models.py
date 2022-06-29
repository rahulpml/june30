
from django.db import models

# Create your models here.
class ProdectDetails(models.Model):
    product_name=models.CharField(max_length=255)
    description=models.TextField()
    quantity=models.IntegerField()
    Price=models.IntegerField()










@property
def image_url(self):
    if self.image and hasattr(self.image, 'url'):
        return self.image_url