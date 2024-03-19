from django.shortcuts import render , redirect
from django.contrib.auth import  login , logout 
from django.contrib.auth.decorators import login_required
from adminportal.forms  import LoginForm
from adminportal.views import init_context
from adminportal.models import ContactMessage
from website.models  import Course


@login_required(login_url="admin-login")
@init_context
def admin_index(request , context):    
    courses = Course.objects.all()
    context['dashboard_cards'] = [
        {
            "title" : "Courses" ,
            "icon" : "bi bi-tools" ,
            "trend_rate" : "5%" ,
            "value" :courses.count()
        } ,
       
    ]
    context['courses'] = courses
    return render(request , "adminportal/index.html" , context=context) 


def admin_login(request):
    context ={}
    if request.method == "POST":
        form = LoginForm(request.POST) 
        if form.is_valid():
            user = form.cleaned_data.get("user")
            login(request , user)
            return  redirect("admin-index")
        else:
            context['errors'] = form.errors_array()
    return render(request , "adminportal/login.html" , context=context)

def admin_logout(request):
    logout(request)
    return redirect("admin-login")

from adminportal.views  import  convert_to_webp

@init_context
def admin_contact_messages(request , context):
    context['contact_messages'] = ContactMessage.objects.all()
    return render(request , "adminportal/contact_messages.html" , context=context)




