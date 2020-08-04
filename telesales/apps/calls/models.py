from django.db import models
from datetime import datetime

# Create your models here.


class Call(models.Model):
    caller_name = models.CharField(max_length=255)
    caller_email = models.EmailField()
    caller_phone = models.CharField(max_length=255)
    disposition = models.CharField(max_length=255)
    caller_details = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    callback_date = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
