from django.db import models
class decorationlist(models.Model):
    title=models.CharField(max_length=250)
    price=models.IntegerField()
    description=models.CharField(max_length=300)
    def __str__(self):
        return self.title 
    

    

