from django import forms
from adminportal.forms  import  BaseForm 
from adminportal.models  import Registration
from website.models import Course

class RegistrationForm(BaseForm):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20 , required=False)
    course_id = forms.CharField(max_length=200)
    id_doc = forms.ImageField(required=False)
    passport = forms.ImageField(required=False)


    def __init__(self , *args , **kwargs):
        self.course = None
        super().__init__(*args , **kwargs)

    def clean_course(self):
        course_id = self.cleaned_data['course_id']
        course = Course.objects.filter(id=course_id).first()
        if not course:
            raise forms.ValidationError("Course not found please select a valid course")
        return course_id 


    # def clean_id_doc(self):
    #     if not self.cleaned_data['id_doc']:
    #         raise forms.ValidationError("Please upload your id document")
    #     return self.cleaned_data['id_doc']
    
    # def clean_passport(self):
    #     if not self.cleaned_data['passport']:
    #         raise forms.ValidationError("Please upload your passport")
    #     return self.cleaned_data['passport']
    


    def save(self):
        data = self.cleaned_data
        course = Course.objects.filter(id=data['course_id']).first()
        self.course = course
        registration = Registration.objects.create(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            course=self.course ,
            id_doc=data['id_doc'],
            passport=data['passport']
        )
        return registration
          

    