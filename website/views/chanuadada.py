from django.shortcuts import render
from website.views import init_website_context

@init_website_context
def chanuadada(request ,context):
    return render(request, 'chanuadada.html' , context=context)


