from django.db import models

# Create your models here.
class Frame(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=30)
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    def __str__(self):
        return self.title