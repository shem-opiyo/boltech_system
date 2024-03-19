from  django.db import  models 
from  adminportal.models import  BaseModel
from website.models import Course

class Registration(BaseModel):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    course = models.ForeignKey(Course , on_delete=models.CASCADE)
    id_doc = models.ImageField(upload_to='registrations/id_docs' , blank=True , null=True)
    passport = models.ImageField(upload_to='registrations/passports' , blank=True , null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Registrations"
        verbose_name = "Registration"
        ordering = ['-created_at']

    

