from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    distance = models.FloatField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    report_url = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.start_location} - {self.end_location}"
        

