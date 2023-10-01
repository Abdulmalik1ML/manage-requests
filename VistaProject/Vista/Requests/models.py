from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=2048)
    description=models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    
class ServiceRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status_choise = (("Pending", "Pending"), ("In progress", "In progress"), ("Completed", "Completed"),)
    status = models.CharField(max_length=300, choices=status_choise , default="Pending")




