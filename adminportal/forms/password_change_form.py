# from django import forms
# from portfolio.models import  PortfolioUser
# class PasswordChangeForm(forms.Form):
#     current_password = forms.CharField(max_length=254)
#     password = forms.CharField(max_length=254)
#     confirm_password = forms.CharField(max_length=254)
    
#     class Meta:
#         fields = "__all__" 

#     def __init__(self  ,user:PortfolioUser , *args , **kwargs):
#         self.user = user
#         super().__init__(*args , **kwargs)
        
#     def errors_array(self):
#         return [f"{error}"for field ,error_list in self.errors.items() for error in error_list]

#     def clean(self):
#         cleaned_data = super().clean()
#         current_password = cleaned_data.get('current_password')
#         password = cleaned_data.get('password')
#         confirm_password = cleaned_data.get('confirm_password')

#         if not current_password or not password or not confirm_password:
#             raise forms.ValidationError("All fields are required")
#         if password != confirm_password:
#             raise forms.ValidationError("Password and confirm password must match for security reasons")
#         elif len(password) < 8 or len(confirm_password) < 8:
#             raise forms.ValidationError("Password must be at least 8 characters long for security reasons")
#         elif not self.user.check_password(self.cleaned_data.get('current_password')):
#                 raise forms.ValidationError("Current password is incorrect")
#         return cleaned_data 
    
#     def save(self):
#         if self.user:
#             self.user.set_password(self.cleaned_data.get('password'))
#             self.user.save()
#             return self.user
        
