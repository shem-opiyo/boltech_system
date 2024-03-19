from django.urls import path

from adminportal import  views 

urlpatterns=[
    path('' , views.admin_index ,name="admin-index"),
    path('login/' , views.admin_login , name="admin-login"),
    path('logout/' , views.admin_logout , name="admin-logout"),

    path('courses/' , views.admin_courses , name="admin-courses"),
    path('courses/add/' , views.admin_add_course , name="admin-add-course"),
    path('courses/<str:course_slug>/' , views.admin_view_course , name="admin-view-course"),

    path('events/' , views.admin_events , name="admin-events"),
    path('events/add/' , views.admin_add_event , name="admin-add-event"),
    path('events/<str:event_id>/' , views.admin_view_event , name="admin-view-event"),


    path('blogs/' , views.admin_blogs , name="admin-blogs"),
    path('blogs/add/' , views.admin_add_blog , name="admin-add-blog"),
    path('blogs/<str:blog_id>/' , views.admin_view_blog , name="admin-view-blog"),



    path('company-data/' , views.admin_company_data , name="admin-company-data"),

    path('testimonials/' , views.admin_testimonials , name="admin-testimonials") ,
    path('testimonials/add/'  , views.admin_add_testimonial , name="admin-add-testimonial" ) ,
    path('testimonials/<str:testimonial_slug>/' , views.admin_view_testimonial , name="admin-view-testimonial" ),

    path('contact-messages/' , views.admin_contact_messages , name="admin-contact-messages"),
    path('contact-messages/<str:message_id>/' , views.admin_view_contact_message , name="admin-view-contact-message"),

    # registration 
    path('registrations/' , views.admin_registration , name="admin-registrations"),
    path('registrations/<str:id>/' , views.admin_view_registration , name="admin-view-registration"),

    # Bronchure 
    path('bronchures/' , views.admin_bronchure , name="admin-bronchures"),
    path('bronchures/add/' , views.admin_add_bronchure , name="admin-add-bronchure"),
    path('bronchures/<str:bronchure_id>/' , views.admin_view_bronchure , name="admin-view-bronchure"),
]

