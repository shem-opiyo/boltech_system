from django import forms 

from website.models  import Course

class CourseForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea , initial=None)
    image = forms.ImageField()
    start_on = forms.DateField(required=False)
    duration = forms.IntegerField(required=False)


    class Meta:
        model = Course
    
    def errors_array(self):
        return [f"{field}:{error}" for field ,error_list in self.errors.items() for error in error_list]

    
    def clean_image(self):
        image = self.cleaned_data['image']
        if not image:
            raise forms.ValidationError("Image is required")
        return image
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if not name:
            raise forms.ValidationError("Name is required")
        elif name and Course.objects.filter(name=name).exists():
            raise forms.ValidationError("Course with this Name already exists")
        return name 

    def clean_description(self):
        description = self.cleaned_data['description']
        if description == None  or description.strip() == "":
            raise forms.ValidationError("Description is required")
        return description 
    
    def clean_course(self):
        # check if course with similar name exists
        name = self.cleaned_data['name'].strip()
        if Course.objects.filter(name=name).exists():
            raise forms.ValidationError("Course with this Name already exists")
        return name   


    def save(self, user= None , commit=True):
        print(self.cleaned_data)
        name = self.cleaned_data['name']
        description = self.cleaned_data['description']
        image = self.cleaned_data['image']
        start_on = self.cleaned_data['start_on']
        duration = self.cleaned_data['duration']
        course = Course(name=name, description=description, image=image,
                        start_on=start_on , duration=duration)
        course.save() 
        self.course = course
        return course

