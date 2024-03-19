from django import forms
from adminportal.models import Testimonial

class TestimonialForm(forms.Form):
    testifier = forms.CharField(max_length=100)
    testifier_role = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    class Meta:
        model = Testimonial 

    def errors_array(self):
            return [f"{field}:{error}" for field ,error_list in self.errors.items() for error in error_list]
            
        

    def clean_testifier(self):
        testifier = self.cleaned_data.get("testifier")
        if  testifier in ["", None]:
            raise forms.ValidationError("Testifier cannot be empty.")
        if Testimonial.objects.filter(testifier=testifier).exists():
            raise forms.ValidationError("Testifier already exists.")
        return testifier
    
    def clean_testifier_role(self):
        testifier_role = self.cleaned_data.get("testifier_role")
        if testifier_role in ["", None]:
            raise forms.ValidationError("Testifier role cannot be empty.")
        # if Testimonial.objects.filter(testifier_role=testifier_role).exists():
        #     raise forms.ValidationError("Testifier role already exists.")
        return testifier_role
    
    def clean_description(self):
        description = self.cleaned_data.get("description")
        if description in ["", None]:
            raise forms.ValidationError("Description cannot be empty.")
        if Testimonial.objects.filter(description=description).exists():
            raise forms.ValidationError("Description already exists.")
        return description

    def save(self):
        testifier = self.cleaned_data.get("testifier")
        testifier_role = self.cleaned_data.get("testifier_role")
        description = self.cleaned_data.get("description")
        image = self.cleaned_data.get("image")
        Testimonial.objects.create(
            testifier=testifier , testifier_role=testifier_role , 
            description=description , image=image )
        