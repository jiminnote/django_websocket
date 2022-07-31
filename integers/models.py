from django.db import models

# Create your models here.
class Integer(models.Model):   
    random = models.IntegerField()


    class Meta:
        db_table = 'integers'