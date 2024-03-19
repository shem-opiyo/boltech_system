from typing import Set
from website.models import BaseModel
from django.db import models

class Blog(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True , blank=True)
    image = models.ImageField(upload_to='blogs' , null=True , blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blogs'

    def save(self, *args, **kwargs):
        self.title=self.title.upper()
        return super().save(*args, **kwargs)

    def  get_absolute_url(self):
        return f"/blog/{self.id}/"