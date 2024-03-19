from django.shortcuts import render , redirect 
from website.models  import Event
from website.views import init_website_context

@init_website_context
def events(request ,context):
    context['events'] =  Event.objects.all()
    return render(request, 'events.html' , context=context)
@init_website_context
def events_details(request ,context, event_id):
    event = Event.objects.filter(id=event_id).first()
    if not event:
        return  redirect("events")
    
    context['event'] =  event
    
    return render(request, 'events-details.html' , context=context)
