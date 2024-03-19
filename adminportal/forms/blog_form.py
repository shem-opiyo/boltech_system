from django import forms
from website.models   import Blog 
from adminportal.forms import  BaseForm


class BlogForm(BaseForm):
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)

    def __init__(self , *args , **kwargs):
        self.blog = kwargs.pop('blog' , None)
        super().__init__(*args , **kwargs)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Blog.objects.filter(title=title).exists() and not self.blog:
            raise forms.ValidationError("Blog with this title already exists.")
        return title

    def clean_description(self):
        description = self.cleaned_data.get('description')
        print(f"===== CLEANING DESCRIPTION {description} =====")
        if  not description:
            raise forms.ValidationError("Description is required.")
        return description
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if  not image and  not self.blog:
            raise forms.ValidationError("Image is required.")
        return image
    
    def save(self , commit=True):
        print(f"Blog description is {self.cleaned_data.get('description')}")
        blog = None
        if not self.blog:
            blog = Blog(
                title = self.cleaned_data.get('title'),
                description = self.cleaned_data.get('description'),
                image = self.cleaned_data.get('image'),
            )
        else:
            blog = self.blog
            blog.title = self.cleaned_data.get('title')
            blog.description = self.cleaned_data.get('description')
            if self.cleaned_data.get('image'):
                blog.image = self.cleaned_data.get('image')
        if commit:
            blog.save()
        self.blog = blog
        return blog



