from django import forms 
from website.models   import Event
from adminportal.forms import  BaseForm

class EventForm(BaseForm):
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)
    date = forms.DateField()
    start_time = forms.TimeField()
    end_time = forms.TimeField()
    # location = forms.CharField(max_length=255 , required=False)

    def __init__(self , *args , **kwargs):
        self.event = kwargs.pop('event' , None)
        super().__init__(*args , **kwargs)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Event.objects.filter(title=title).exists() and not self.event:
            raise forms.ValidationError("Event with this title already exists.")
        return title
    
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if  not description:
            raise forms.ValidationError("Description is required.")
        return description
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if  not image and  not self.event:
            raise forms.ValidationError("Image is required.")
        return image
    
    def clean_date(self):
        date = self.cleaned_data.get('date')
        if  not date:
            raise forms.ValidationError("Event Date is required.")
        return date 
    
    def clean_start_time(self):
        start_time = self.cleaned_data.get('start_time')
        if  not start_time:
            raise forms.ValidationError("Start Time is required.")
        return start_time
    
    def clean_end_time(self):
        end_time = self.cleaned_data.get('end_time')
        if  not end_time:
            raise forms.ValidationError("End Time is required.")
        return end_time

    def save(self , commit=True):
        event = None
        if self.event:
            event = self.event
            event.title = self.cleaned_data.get('title')
            event.description = self.cleaned_data.get('description')
            if self.cleaned_data.get('image'):
                event.image = self.cleaned_data.get('image')
            if self.cleaned_data.get('date'):
                event.date = self.cleaned_data.get('date')
            if self.cleaned_data.get('start_time'):
                event.start_time = self.cleaned_data.get('start_time')
            if self.cleaned_data.get('end_time'):
                event.end_time = self.cleaned_data.get('end_time')
            if self.cleaned_data.get('location'):
                event.location = self.cleaned_data.get('location')
             
        else:
            event = Event(
                title = self.cleaned_data.get('title'),
                description = self.cleaned_data.get('description'),
                image = self.cleaned_data.get('image'),
                date = self.cleaned_data.get('date'),
                start_time = self.cleaned_data.get('start_time'),
                end_time = self.cleaned_data.get('end_time'),
                # location = self.cleaned_data.get('location'),
            )
        if commit:
            event.save()
        self.event = event
        return event