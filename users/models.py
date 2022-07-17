from django.db import models

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(TimeStampModel):
    name     = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    email    = models.EmailField(max_length=128)

    class Meta :
        db_table = 'users'