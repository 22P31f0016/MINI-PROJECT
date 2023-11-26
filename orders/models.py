from django.db import models
from products.models import decorationlist
class orderlist(models.Model):
    product=models.OneToOneField(decorationlist,on_delete=models.CASCADE,default=1)

def __str__(self):
    return self.product.title