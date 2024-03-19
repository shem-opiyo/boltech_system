from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from adminportal.views import init_context , javascript_redirect
from website.models import Blog
from adminportal.forms import BlogForm 


@init_context
def admin_blogs(request , context):
    blogs = Blog.objects.all().order_by('-created_at')
    context['blogs'] = blogs
    return render(request , 'adminportal/blogs/index.html' , context)

@init_context
def admin_add_blog(request , context):
    if request.method == "POST":
        form = BlogForm(request.POST , request.FILES)
        if form.is_valid():
            blog = form.save(request.user)
            context['blog'] = blog
            context['messages'] = ["Blog Added Successfully"]
            context = javascript_redirect(context ,
                    reverse("admin-view-blog" , kwargs={"blog_id":blog.id}))
          
        else:
            context['errors'] = form.errors_array()
    return render(request , 'adminportal/blogs/add.html' , context)


@init_context
def admin_view_blog(request , context , blog_id):
    blog = Blog.objects.filter(id=blog_id).first()
    if not blog :
        return redirect("admin-blogs")
    context['blog'] = blog
    if request.method == "POST":
        action = request.POST.get("action")

        # print(request.POST)
        if action  == "edit":
            form = BlogForm(request.POST , request.FILES , blog=blog)
            if form.is_valid():
                blog = form.save()
                context['blog'] = blog 
                context['messages'] = ["Blog Updated Successfully"]
                context = javascript_redirect(context ,
                        reverse("admin-view-blog" , kwargs={"blog_id":blog.id}))
            else:
                context['errors'] = form.errors_array()
        elif action == "delete":
            blog.delete()
            context['messages'] = ["Blog Deleted Successfully"]
            context = javascript_redirect(context , reverse("admin-blogs"))
    return render(request , 'adminportal/blogs/view.html' , context)