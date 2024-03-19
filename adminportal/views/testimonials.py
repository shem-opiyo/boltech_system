from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect
from django.urls import reverse
from adminportal.models  import Testimonial
from adminportal.forms import TestimonialForm , TestimonialEditForm
from adminportal.views import init_context , javascript_redirect


#  Testimonials section 
@login_required(login_url="admin-login")
@init_context
def admin_testimonials(request , context):
    context['testimonials'] = Testimonial.objects.all().order_by("-id")
    return render(request , "adminportal/testimonials/index.html" , context=context)

@login_required(login_url="admin-login")
@init_context
def admin_add_testimonial(request , context):
    if request.method == "POST":
        form = TestimonialForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            context['messages'] = ["Testimonial added successfully."]
            context = javascript_redirect(context , reverse("admin-testimonials"))
        else:
            context['errors'] = form.errors_array()
    return render(request , "adminportal/testimonials/add_testimonial.html" , context=context)

@login_required(login_url="admin-login")
@init_context
def admin_view_testimonial(request , context , testimonial_slug):
    testimonial = Testimonial.objects.filter(slug=testimonial_slug).first()
    if testimonial:
      if request.method == "POST":
            action = request.POST.get("action")
            if action == "delete":
              testimonial.delete()
              context['messages'] = ["Testimonial deleted successfully."]
              context['script'] =javascript_redirect(context , reverse("admin-testimonials"))
            elif action == "edit":
                form = TestimonialEditForm(request.POST , request.FILES)
                if form.is_valid():
                    form.save(testimonial=testimonial)
                    context['messages'] = ["Testimonial updated successfully."]
                else:
                    context['errors'] = form.errors_array()

      context['testimonial'] = testimonial
      return render(request , "adminportal/testimonials/view_testimonial.html" , context=context)
    else:
        return redirect("admin-testimonials")
