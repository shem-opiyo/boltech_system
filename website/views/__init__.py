from  functools  import  wraps
from adminportal.models import Bronchure 
def init_website_context(func):
    @wraps(func)
    def wrapper(request , *args , **kwargs):
        context = {}
        context["bronchure"] = Bronchure.objects.last()
        return func(request , context , *args , **kwargs)
    return wrapper


from  .index import index
from  .about import about
from  .contact import contact
from  .courses import courses ,course_details
from  .events import events ,events_details
from  .blog import blog , blog_details
from  .chanuadada import chanuadada
from  .register import register

