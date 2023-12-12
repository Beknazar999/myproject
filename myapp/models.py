from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    
    
    
# models.py
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


from django.db import models

class YourModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
