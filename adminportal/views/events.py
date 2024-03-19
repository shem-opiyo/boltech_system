from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

from adminportal.forms import EventForm
from website.models import Event

from adminportal.views  import  init_context
from adminportal import  logger 

@init_context
def admin_events(request ,context):
    events = Event.objects.all()
    return render(request , 'adminportal/events/index.html' , {'events':events})

@init_context
def admin_add_event(request ,context):
    if request.method == 'POST':
        form = EventForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin-events')
        context['errors'] = form.errors_array()
        context['form_data'] = form.cleaned_data
    return render(request , 'adminportal/events/add.html' ,context=context)

@init_context
def admin_view_event(request ,context , event_id):
    event = Event.objects.filter(id=event_id).first()
    if not event:
        return redirect('admin-events')
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'delete':
            event.delete()
            return redirect('admin-events')
        elif action == 'edit':
            logger.info("Editing event with id: %s" % event_id)
            form = EventForm(request.POST , request.FILES , event=event)
            if form.is_valid():
                form.save()
                return redirect('admin-events')
            context['errors'] = form.errors_array()
    context['event'] = event
    return render(request , 'adminportal/events/view.html' ,context=context)

