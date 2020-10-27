from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=250)
    notes = models.TextField()
    add_time = models.DateTimeField(auto_now=True)
