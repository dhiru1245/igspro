from django.db import models



class ContactData(models.Model):
    name = models.CharField(max_length=200)
    add = models.CharField(max_length=200)
    email = models.EmailField()
    mob = models.BigIntegerField()
    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=200)
    deg = models.CharField(max_length=200)
    imgage = models.ImageField(upload_to="images/")






class FeedbackData(models.Model):
    name = models.CharField(max_length=20)
    rating = models.IntegerField()
    time = models.DateField(auto_now=True)
    feedback = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class ImageData(models.Model):
    image = models.ImageField(upload_to="images/")


class GraphData(models.Model):
    block_name  = models.CharField(max_length=200)
    yf = models.IntegerField()
    awc = models.IntegerField()
    cc = models.IntegerField()

