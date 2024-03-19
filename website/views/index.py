from django.shortcuts import render
from adminportal.models  import Testimonial ,ContactMessage
from website.models import Course ,Event
from website.views import init_website_context

@init_website_context
def index(request ,context):
    testimonials = Testimonial.objects.all().order_by("created_at")
    courses = Course.objects.all().order_by('created_at')[:4]
    context['courses'] =  courses
    context['testimonials'] =  testimonials
    context['events'] =  Event.objects.all().order_by('date')[:4]
    

    if request.method == "POST":
        data = request.POST
        action = data.get('action')
        
        if action  == "inquiry":
            inquiry_message = ContactMessage.objects.create(
                name = data.get("name") ,
                subject = data.get("subject") ,
                email= data.get("email") ,
                message = data.get("message") ,
                type =" inquiry"
            )
            context["messages"] = [
                f"Thank you for your inquiry {inquiry_message.name} we will get back to you soon"
            ]
    return render(request, 'index.html' , context=context)



