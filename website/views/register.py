from adminportal.forms import RegistrationForm 
from django.shortcuts import render , redirect 
from website.models import Course 
from website.views import init_website_context

@init_website_context
def register(request ,context):
    context["courses"] = Course.objects.all()
    if request.method == "POST":
        form = RegistrationForm(request.POST , request.FILES)
        if form.is_valid():
            register  = form.save() 
            print("======NEw User registered=====")
            context['messages'] = [f"Congratulations {register.name} your Application for {register.course.name} has been submitted successfully"]
        else:
            context['errors'] = form.errors_array()
        return render(request , "register.html" , context=context)
    else:
        return render(request ,"register.html" , context=context)
            
