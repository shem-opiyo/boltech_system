from django import  forms 
from website.models  import Course

class CourseEditForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea , initial=None)
    image = forms.ImageField()
    start_on = forms.DateField(required=False)
    duration = forms.IntegerField(required=False)


    class Meta:
        model = Course
        fields = ['name', 'description', 'image', 'type']
    
    def __init__(self , *args , **kwargs):
        self.course = kwargs.pop('course' , None) if kwargs.get('course') else None
        super().__init__(*args , **kwargs)
        if self.course:
            self.fields['name'].initial = self.course.name
            self.fields['description'].initial = self.course.description
            self.fields['image'].initial = self.course.image 
           
    
    def errors_array(self):
        return [f"{field}:{error}" for field ,error_list in self.errors.items() for error in error_list]
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if name == None  or name.strip() == "":
            raise forms.ValidationError("Name is required")
        return name


    
    def clean_description(self):
        description = self.cleaned_data['description']
        if description == None  or description.strip() == "":
            raise forms.ValidationError("Description is required")
        return description 

    def save(self):
        self.course.name = self.cleaned_data['name']
        self.course.description = self.cleaned_data['description']
        self.course.start_on = self.cleaned_data['start_on']
        self.course.duration = self.cleaned_data['duration']

        if self.cleaned_data['image']:
            self.course.image = self.cleaned_data['image']
        self.course.save()
        return self.course



