from adminportal.models  import  BaseModel
from django.db  import  models 


class Bronchure(BaseModel):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="bronchures") 

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = "Bronchure"
        verbose_name_plural = "Bronchures" 
        ordering = ['-created_at']




