from django.shortcuts import render , redirect
from adminportal.models import ContactMessage
from website.views import init_website_context

@init_website_context
def contact(request ,context):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        subject = data.get("subject")
        # phone = data.get('phone')
        
        if name and email and message:
            contact_message = ContactMessage.objects.create(
                name=name,
                subject = subject ,
                email=email,
                message=message
            )
            contact_message.save()
            context['messages'] = [f"Thank you {name} for contacting us. We will get back to you soon."]
        else:
            return redirect("contact")
        
    return render(request, 'contact.html'  , context=context)


