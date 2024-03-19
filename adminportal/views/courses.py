from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.urls import reverse

from website.models  import Course

from adminportal.views import init_context ,javascript_redirect
from adminportal.forms import CourseForm  ,CourseEditForm
# class view for displaying the  list of courses

@login_required(login_url="admin-login")
@init_context 
def admin_courses(request , context):
    courses = Course.objects.all()
    context['courses'] = courses
    return render(request , "adminportal/courses/index.html" , context=context) 

@login_required(login_url="admin-login")
@init_context
def admin_add_course(request , context):
    if request.method == "POST":
        form = CourseForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            context['messages'] = ["Course added successfully"]
            context = javascript_redirect(context ,
                reverse("admin-view-course" , 
                        kwargs={"course_slug":form.course.slug}))
        else:
            context['errors'] = form.errors_array()
    return render(request , "adminportal/courses/add.html" , context=context)

@login_required(login_url="admin-login")
@init_context
def admin_view_course(request , context ,course_slug):
    course = Course.objects.filter(slug=course_slug).first()
    if course:
        context['course'] = course 

        if request.method == "POST":
            action = request.POST.get("action")
            if action == "edit":
                form = CourseEditForm(request.POST , request.FILES , course=course)
                if form.is_valid():
                    form.save()
                    context['messages'] = ["Course updated successfully"]
                    context = javascript_redirect(context ,
                        reverse("admin-view-course" , 
                                kwargs={"course_slug":form.course.slug}))
                else:
                    context['errors'] = form.errors_array()
                    
            elif action == "delete":
                course.delete()
                context['messages'] = ["Course deleted successfully"]
                context = javascript_redirect(context , reverse("admin-courses"))
    else:
        return redirect("admin-courses")
    return render(request , "adminportal/courses/view.html" , context=context)




