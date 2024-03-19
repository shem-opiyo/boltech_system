from django.shortcuts import render
from adminportal.models  import Testimonial
from website.views import init_website_context

@init_website_context
def about(request ,context):
    testimonials = Testimonial.objects.all().order_by("created_at")
    context = {
        'testimonials': testimonials
    }
    return render(request, 'about-us.html' , context=context)
