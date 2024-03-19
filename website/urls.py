from django.urls import path
from website import views 
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', csrf_exempt(views.index), name='index'),
    path('about/', views.about, name='about'),
    path('contact/',csrf_exempt(views.contact), name='contact'), 
    path('course-details/<course_slug>/',views.course_details, name='course-details'),
    path('courses/',views.courses, name='courses'),
    path('events/',views.events, name='events'),
    path('events/<str:event_id>/',views.events_details, name='event-details'),
    path('blog/',views.blog, name='blog'),
    path('blog/<str:blog_id>/',views.blog_details, name='blog-details'),
    path('chanuadada/',views.chanuadada, name='chanuadada'), 

    path('register/', csrf_exempt(views.register) , name='register'),

]