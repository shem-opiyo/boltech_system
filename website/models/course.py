from website.models import BaseModel
from django.db import models 
from django.utils.text import slugify
from django.utils import timezone

class Course(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True , blank=True)
    start_on = models.DateField(null=True , blank=True , default=timezone.now)
    duration = models.IntegerField() # in months
    image = models.ImageField(upload_to='courses' , null=True , blank=True)
    slug = models.SlugField(max_length=2550 , null = True , blank = True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return f"/course-details/{self.slug}/"

    class Meta:
        db_table = 'courses'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        self.name=self.name.upper()
        return super().save(*args, **kwargs)