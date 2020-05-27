from django.db import models

# Create your models here.
class CSS(models.Model):
    #image = models.ImageField(upload_to="mainpage/", blank=True, null=True)
    title = models.CharField(max_length=70)
    area = models.CharField(max_length=70)
    time = models.CharField(max_length=70)
    mood = models.CharField(max_length=70)
    floor = models.CharField(max_length=70)
    Choice = (
        ('yes', '있음'),
        ('no', ' 없음'),
    )
    Petchoice = (
        ('yes', '출입가능'),
        ('no', '출입금지'),
    )
    toilet = models.CharField(max_length=3, choices=Choice)
    smoke = models.CharField(max_length=3, choices=Choice)
    elevator = models.CharField(max_length=3, choices=Choice)
    pet = models.CharField(max_length=4, choices=Choice)
    add = models.TextField()
    image = models.ImageField(upload_to= "css/" , null= True, blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.add[:100]