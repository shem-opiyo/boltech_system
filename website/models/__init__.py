from django.db   import models
from django.utils  import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract=True

    def save(self, *args, **kwargs):
        obj_exists = self.__class__.objects.filter(pk=self.pk).exists()
        if obj_exists:
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)

from  .course import Course
from  .blog  import  Blog 
from  .event import Event 





