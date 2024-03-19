from django.shortcuts import render , redirect 
from website.models import Course
from website.views import init_website_context


@init_website_context
def course_details(request ,context , course_slug):
    print(f"====={course_slug}=====")
    course = Course.objects.filter(slug=course_slug).first()
    if  not course:
        return redirect("courses")
    context['course'] =  course 
    context['popular_courses']  = Course.objects.all().order_by('-created_at')
        
    return render(request, 'course-details.html' , context=context)
    
@init_website_context
def courses(request ,context):
    context['courses']   =  Course.objects.all().order_by('-created_at')
    
    return render(request, 'courses.html' , context=context)
