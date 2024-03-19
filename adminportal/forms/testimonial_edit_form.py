from django import forms
from adminportal.models import Testimonial
from adminportal.forms  import BaseForm 

class TestimonialEditForm(BaseForm):
    testifier = forms.CharField(max_length=100)
    testifier_role = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(initial=None , required=False)
    class Meta:
        model = Testimonial 



    def save(self , testimonial=None):
        if  testimonial != None :
            testimonial.testifier = self.cleaned_data.get("testifier")
            testimonial.testifier_role = self.cleaned_data.get("testifier_role")
            testimonial.description = self.cleaned_data.get("description")
            if  self.cleaned_data.get("image") != None:
                 testimonial.image = self.cleaned_data.get("image")
            testimonial.save()