from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from adminportal.views import init_context , javascript_redirect
# from adminportal.forms import ProfileEditForm , CompanyAboutForm
# from adminportal.forms import  AddressForm


@login_required(login_url="admin-login")
@init_context 
def admin_company_data(request , context):
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "update_profile":
            form = ProfileEditForm(request.POST)
            if form.is_valid():
                form.save()
                context['messages'] = ["Company profile updated successfully"]
                context = javascript_redirect(context , reverse("admin-company-data") , delay=3000)
            else:
                context['messages'] = form.errors_array()
        elif action == "update_about":
            form = CompanyAboutForm(request.POST , request.FILES)
            if form.is_valid():
                form.save()
                context['messages'] = ["Company about updated successfully"]
                context = javascript_redirect(context , reverse("admin-company-data") , delay=3000)
            else:
                context['errors'] = form.errors_array() 

        elif action == "update_address":
            form = AddressForm(request.POST)
            if form.is_valid():
                form.save()
                context['messages'] = ["Company address updated successfully"]
                context = javascript_redirect(context , reverse("admin-company-data") , delay=3000)
            else:
                context['errors'] = form.errors_array()
                
    return render(request ,"adminportal/company/index.html" , context=context)