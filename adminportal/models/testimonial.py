from django.db  import  models 
from website.models  import  BaseModel
from django.utils.text import slugify


class Testimonial(BaseModel):
    testifier = models.CharField(max_length=254)
    testifier_role = models.CharField(max_length=254)
    description = models.TextField()
    slug = models.CharField(max_length=254 ,null=True , blank=True)
    image = models.ImageField(upload_to="testimonials")


    class Meta:
        db_table="testimonial"

    def save(self , *args , **kwargs):
        self.slug = slugify(self.testifier)
        self.slug = self.slug.replace("." , "-")
        super().save(*args, **kwargs)

    def __str__(self):
        return  self.testifier




