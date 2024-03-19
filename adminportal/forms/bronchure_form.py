from adminportal.forms  import  BaseForm
from django  import   forms   
from adminportal.models import  Bronchure

class BronchureForm(BaseForm):
    name = forms.CharField(max_length=100)
    file = forms.FileField(required=False)

    def __init__(self , *args , **kwargs):
        self.bronchure = None 
        self.bronchure = kwargs.pop("bronchure" , None)
        super().__init__(*args , **kwargs)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if not name:
            raise forms.ValidationError("Name is required")
        return name
    
    def clean_file(self):
        file = self.cleaned_data.get("file")
        if  not self.bronchure and file is None:
            if not file :
                raise forms.ValidationError("File is required")
            # checking if the file type  is a pdf
            if not file.endswith(".pdf"):
                raise forms.ValidationError("File must be a pdf")
        return file

    def save(self):
        name = self.cleaned_data.get("name")
        file = self.cleaned_data.get("file")

        if  self.bronchure:
            self.bronchure.name = name 
            if  file:
                self.bronchure.file = file 
            self.bronchure.save()
            return self.bronchure
        else:
            bronchure = Bronchure.objects.create(
                name = name ,
                file = file 
            )
            return bronchure


