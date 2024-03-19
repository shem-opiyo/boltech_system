from django import forms

class BaseForm(forms.Form):
        def errors_array(self):
                """
                - Unpacks the form errors to a more readable format
                - Returns an array of  strings

                """
                return [f"{field} : ({error}"for field ,error_list in self.errors.items() for error in error_list]
        class Meta:
                abstract = True


from .login_form import * 
from .course_form import *
from  .testimonial_form import *
# from  .profile_edit_form import *
# from .password_change_form import *
from .course_edit_form import *
from .testimonial_edit_form import *

from .event_form import *
from .blog_form import *
from .registration_form import RegistrationForm
from  .bronchure_form import BronchureForm



