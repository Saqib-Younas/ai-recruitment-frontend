from django.db import models

# Testimonial Model (Spelling check karein: T-e-s-t-i-m-o-n-i-a-l)
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100) # Jaise 'HR Manager'
    message = models.TextField()
    rating = models.IntegerField(default=5)
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)

    def __str__(self):
        return self.name

# FAQ Model
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question