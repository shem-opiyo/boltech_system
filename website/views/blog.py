from django.shortcuts import render , redirect
from website.models  import Blog
from website.views import init_website_context

@init_website_context
def blog(request ,context):
    context["blogs"] =  Blog.objects.all()
    return render(request, 'blog.html' , context=context)

@init_website_context
def blog_details(request ,context , blog_id):
    blog = Blog.objects.filter(id=blog_id).first()
    print(f"====== {blog} ======")
    if not blog:
        return redirect("blog")
    context["blog"]   =  blog
    return render(request, 'blog-details.html' , context=context)





