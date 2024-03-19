from functools import wraps
from PIL import Image
from django.core.files import File
from adminportal.models import AdminUser


def init_context(func):
    @wraps(func)
    def wrapper(request , *args , **kwargs):
        context = {}
        admin_user = request.user 
        if admin_user and admin_user.is_authenticated :
            if not AdminUser.objects.filter(id=admin_user.id).exists():
                return redirect("admin-login")
            context['admin_user'] = admin_user
            return func(request , context , *args , **kwargs)
        else:
            return redirect("admin-login")
    return wrapper

def javascript_redirect(context , url , delay=1000):
    print(f"javascript_redirect url  is {url}")
    context['script'] = f"""
    setTimeout(function(){{
        window.location.href="{url}"
    }}, {delay});
    """ 
    return context

def convert_to_webp(source):
    """Convert image to WebP.

    Args:
        source (django.core.files.File): Source image file

    Returns:
        django.core.files.File: Path to the new image file
    """
    destination = source.name.split(".")[0] + ".webp"

    image = Image.open(source)  # Open image
    webp_temp_path = f"temp/{destination}"  # Temporary path for the converted image
    image.save(webp_temp_path, format="webp")  # Convert image to webp

    destination_file = File(open(webp_temp_path, "rb"))  # Create a Django File object
    destination_file.name = destination  # Set the file name

    return destination_file


from .home  import *
from .courses import *
from .events import *
from .blog  import *
from .company import *
from .testimonials import *
from .contact_messages import *
from .registration import  *
from .bronchure import  *


