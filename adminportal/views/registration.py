from adminportal.forms import RegistrationForm 
from adminportal.models import Registration
from django.shortcuts import render , redirect



def  admin_registration(request):
    registrations = Registration.objects.all()
    context = {
        'registrations':registrations
    }
    return render(request , "adminportal/registration/index.html" , context=context)

def admin_view_registration(request , id):
    registration = Registration.objects.filter(id=id).first()
    if  not registration:
        return redirect("admin-registrations")
    context = {
        'registration':registration
    }
    return render(request , "adminportal/registration/view.html" , context=context)

