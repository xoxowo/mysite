from django.db import models

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Post(TimeStampModel):
    title    = models.CharField(max_length=100)
    text     = models.TextField()
    name     = models.CharField(max_length=50)
    password = models.CharField(max_length=200)

    class Meta :
        db_table = 'postings'