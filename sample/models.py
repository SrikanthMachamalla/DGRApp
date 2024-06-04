from django.db import models

class Excel(models.Model):
    file = models.FileField(upload_to='uploads/')

class Table1File(models.Model):
    file = models.FileField(upload_to='uploads/')
    
class Table3File(models.Model):
    file = models.FileField(upload_to='uploads/')
    

