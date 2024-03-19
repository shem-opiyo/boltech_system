from django import forms
from adminportal.models  import AdminUser 
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = AdminUser.objects.filter(username=username).first()
            if not user :
                raise forms.ValidationError("Invalid username or password.")
            if not check_password(password , user.password):
                raise forms.ValidationError("Invalid username or password.")
        cleaned_data['user'] = user 
        return cleaned_data

    def errors_array(self):
        return [str(error) for field ,error_list in self.errors.items() for error in error_list]
   