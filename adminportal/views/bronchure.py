from django.shortcuts import render ,redirect 
from adminportal.views  import  init_context
from adminportal.forms  import  BronchureForm
from adminportal.models import  Bronchure

@init_context
def admin_bronchure(request , context):
    bronchures = Bronchure.objects.all()
    context["bronchures"] = bronchures
    
    return render(request , "adminportal/bronchure/index.html" , context=context)

@init_context
def admin_add_bronchure(request , context):
    if request.method == "POST":
        form = BronchureForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            context["messages"] = ["Bronchure added successfully"]
        else:
            context["errors"] = form.errors_array()

    return render(request , "adminportal/bronchure/add.html" , context=context)

@init_context
def admin_view_bronchure(request , context , bronchure_id):
    bronchure = Bronchure.objects.filter(id=bronchure_id).first()
    if  not bronchure:
        return redirect("admin-bronchures")
    context["bronchure"] = bronchure

    if  request.method == "POST":
        action = request.POST.get("action")
        if action == "edit":
            form = BronchureForm(request.POST , request.FILES , bronchure=bronchure)
            if form.is_valid():
                form.save()
                context["messages"] = ["Bronchure updated successfully"]
            else:
                context["errors"] = form.errors_array()
        elif action == "delete":
            bronchure.delete()
            context["messages"] = ["Bronchure deleted successfully"]
            return redirect("admin-bronchures")
    return render(request , "adminportal/bronchure/view.html" , context=context)



