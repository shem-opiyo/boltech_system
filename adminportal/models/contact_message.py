from django.db  import  models 
from django.utils.text import slugify
from website.models  import  BaseModel

class ContactMessage(BaseModel):
    name = models.CharField(max_length=254)
    email = models.EmailField()
    phone = models.CharField(max_length=254 , null=True , blank=True)
    subject  = models.TextField(null=True , blank=True)
    message = models.TextField()
    type = models.CharField(null=True , blank=True , default="message" , max_length=254)
    # slug = models.CharField(max_length=254)
    

    class Meta:
        db_table="contact_message"
    
    def __str__(self):
        return self.name 

    def save(self , *args , **kwargs):
        # self.slug = slugify(self.name)
        super().save(*args , **kwargs)
