from  django.shortcuts import render , redirect 
from adminportal.views import init_context
from django.contrib.auth.decorators import login_required
from adminportal.views import init_context
from adminportal.models import ContactMessage
@login_required(login_url="admin-login")
@init_context
def admin_contact_messages(request , context):
    context['contact_messages'] = ContactMessage.objects.all()
    return render(request , "adminportal/contact-messages/index.html" , context=context)


@login_required(login_url="admin-login")
@init_context
def admin_view_contact_message(request , context , message_id):
    contact_message = ContactMessage.objects.filter(id=message_id).first()
    if contact_message:
        if request.method == "POST":
            action = request.POST.get('action')
            if action == "delete":
                contact_message.delete()
                return redirect("admin-contact-messages")
            
        context['contact_message'] = contact_message
        return render(request , "adminportal/contact-messages/view_contact_message.html" , context=context)
    else:
        return redirect("admin-contact-messages") 






