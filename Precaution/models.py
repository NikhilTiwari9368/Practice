
# Create your models here.
from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    precautions = models.TextField()
    what_to_eat = models.TextField()  # What the patient should eat
    daily_exercise = models.TextField()
    exercise_instructions = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='media/Registration/')  # Image related to the disease
    treatment = models.TextField()
    medicine = models.TextField()
    video = models.FileField(upload_to='media/Registration/')


    def __str__(self):
        return self.name

# Create your models here