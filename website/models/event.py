from website.models import BaseModel
from django.db import models
from django.utils.text import slugify

class Event(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True , blank=True)
    image = models.ImageField(upload_to='events' , null=True , blank=True)
    date = models.DateField(null=True , blank=True)
    start_time = models.TimeField(null=True , blank=True)
    end_time = models.TimeField(null=True , blank=True)
    location = models.CharField(max_length=255 , null=True , blank=True , default="Boltech Institute")
    slug = models.CharField(max_length=255 , null=True , blank=True)
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'events'

    def save(self, *args, **kwargs):
        self.title=self.title.title()
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
